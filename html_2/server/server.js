const server = require('http').createServer();
const faker = require('faker');


class Point {

    constructor(x = 0, y = 0) {
        this.x = x;
        this.y = y;
    }

    isEqual(another) {
        return this.x === another.x && this.y === another.y;
    }

    add(another) {
        return new Point(this.x + another.x, this.y + another.y);
    }

    static getRandom() {
        return new Point(Math.ceil(Math.random() * 49) * 10, Math.ceil(Math.random() * 49) * 10);
    }

    isOpposite(another) {
        return (this.x + another.x === 0) && (this.y + another.y === 0);
    }
}

class Snake {
    constructor(name = 'noName') {
        this.name = name;
        this.body = [Point.getRandom()];
    }

    getHead() {
        return this.body[0];
    }

    add(point) {
        this.body.unshift(this.getHead().add(point));
    }

    move(point) {
        let head = this.getHead().add(point);
        if (head.x < 0) {
            head.x = 490;
        }
        if (head.x > 490) {
            head.x = 0;
        }
        if (head.y < 0) {
            head.y = 490;
        }
        if (head.y > 490) {
            head.y = 0;
        }
        this.body.unshift(head);
        this.body.pop();
    }
}

class Direction extends Point {
    move(another) {
        if (!this.isOpposite(another)) {
            this.x = another.x;
            this.y = another.y;
        }
    }
}

let clients = {};
const io = require('socket.io')(server);

let cherry = new Point(-10, -10);
let food = new Point(100, 100);

setInterval(function () {
    cherry = Point.getRandom();
}, 5000);


io.on('connection', function (client) {

    clients[client.id] = {
        dir: new Direction(10, 0),
        snake: new Snake(),
    };
    let snake = clients[client.id].snake;
    let dir = clients[client.id].dir;
    snake.add(dir);
    snake.add(dir);
    snake.color = faker.commerce.color();

    client.on('setName', function (name) {
        snake.name = name;
    });
    client.on('setColor', function (color) {
        snake.color = color;
    });

    var loopId = setInterval(function () {
        if (snake.getHead().isEqual(cherry)) {
            cherry = new Point(-10, -10);
            snake.add(dir);
            snake.add(dir);
        } else if (snake.getHead().isEqual(food)) {
            food = Point.getRandom();
            snake.add(dir);
        } else {
            snake.move(dir);
        }
        client.emit('render', JSON.stringify({ clients, food, cherry }));
    }, 100);

    client.on('move', function (data) {
        switch (data) {
            case 'ArrowRight':
                dir.move(new Point(10, 0));
                break;
            case 'ArrowLeft':
                dir.move(new Point(-10, 0));
                break;
            case 'ArrowUp':
                dir.move(new Point(0, -10));
                break;
            case 'ArrowDown':
                dir.move(new Point(0, 10));
                break;
        }
    });

    client.on('disconnect', () => { /* … */
        delete clients[client.id];
    });

});


server.listen(3000);
