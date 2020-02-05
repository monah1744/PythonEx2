// let socket = io('http://192.168.2.181:3000'); let socket = io('http://192.168.2.181:3000');
// let $field = document.getElementById('field');
// let ctx = $field.getContext('2d');

// class Point {

//     constructor(x = 0, y = 0) {
//         this.x = x;
//         this.y = y;
//     }

//     isEqual(another) {
//         return this.x === another.x && this.y === another.y;
//     }

//     add(another) {
//         return new Point(this.x + another.x, this.y + another.y);
//     }

//     static getRandom() {
//         return new Point(Math.ceil(Math.random() * 49) * 10, Math.ceil(Math.random() * 49) * 10);
//     }

//     isOpposite(another) {
//         return (this.x + another.x === 0) && (this.y + another.y === 0);
//     }
// }

// class Snake {
//     constructor(body) {
//         this.body = body;
//     }

//     getHead() {
//         return this.body[0];
//     }

//     add(point) {
//         this.body.unshift(snake.getHead().add(point));
//     }

//     move(point) {
//         let head = this.getHead().add(dir);
//         if (head.x < 0) {
//             head.x = 490;
//         }
//         if (head.x > 490) {
//             head.x = 0;
//         }
//         if (head.y < 0) {
//             head.y = 490;
//         }
//         if (head.y > 490) {
//             head.y = 0;
//         }
//         this.body.unshift(head);
//         this.body.pop();
//     }
// }

// class Direction extends Point {
//     move(another) {
//         if (!this.isOpposite(another)) {
//             this.x = another.x;
//             this.y = another.y;
//         }
//     }
// }

// let dir = new Direction(10, 0);

// let snake = new Snake([
//     new Point(30, 10),
//     new Point(20, 10),
//     new Point(10, 10),
// ]);

// let cherry = new Point(-10, -10);
// let food = new Point(100, 100);


// let loopId = setInterval(function () {
//     ctx.clearRect(0, 0, 500, 500);

//     if (snake.getHead().isEqual(cherry)) {
//         cherry = new Point(-10, -10);
//         snake.add(dir);
//         snake.add(dir);
//     } else if (snake.getHead().isEqual(food)) {
//         food = Point.getRandom();
//         snake.add(dir);
//     } else {
//         snake.move(dir);
//     }

//     ctx.fillStyle = 'red';
//     ctx.fillRect(cherry.x, cherry.y, 10, 10);

//     ctx.fillStyle = 'green';
//     ctx.fillRect(food.x, food.y, 10, 10);

//     ctx.fillStyle = 'black';
//     for (let block of snake.body) {
//         ctx.fillRect(block.x, block.y, 10, 10);
//     }

//     for (let element of snake.body.slice(1)) {
//         if (element.isEqual(snake.getHead())) {
//             alert('Game over');
//             clearInterval(loopId);
//         }
//     }

//     ctx.fillText('dfgfdgdf', snake.getHead().x + 10, snake.getHead().y - 10);


// }, 100);


// setInterval(function () {
//     cherry = Point.getRandom();
// }, 5000);


// document.addEventListener('keydown', function (event) {

//     switch (event.key) {
//         case 'ArrowRight':
//             dir.move(new Point(10, 0));
//             break;
//         case 'ArrowLeft':
//             dir.move(new Point(-10, 0));
//             break;
//         case 'ArrowUp':
//             dir.move(new Point(0, -10));
//             break;
//         case 'ArrowDown':
//             dir.move(new Point(0, 10));
//             break;
//     }
// });


let socket = io('http://192.168.2.181:3000');
let $field = document.getElementById('field');
let ctx = $field.getContext('2d');

socket.on('render', function (snake) {
    ctx.clearRect(0, 0, 500, 500);
    snake = JSON.parse(snake);
    for (let element of snake.body) {
        ctx.fillRect(element.x, element.y, 10, 10);
    }
});

document.addEventListener('keydown', function (event) {
    socket.emit('move', event.key);
});
