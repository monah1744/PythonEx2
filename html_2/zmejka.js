let $field = document.getElementById('field');
let ctx = $field.getContext('2d');


let head = [10, 10];
let dir = [10, 0];

let body = [[10, 10], [20, 10], [30, 10]];
let cherry = [50, 50];

function move(head, dir) {
    return [head[0] + dir[0], head[1] + dir[1]];
}
setInterval(function () {
    ctx.clearRect(0, 0, 500, 500);
    if (body[0][0] === cherry[0] && body[0][1] === cherry[1]) {
        cherry = [-10, 10];
        body.unshift(move(body[0], dir));
    }
    else {
        body.unshift(move(body[0], dir));
        body.pop();
    }
    ctx.fillStyle = 'red';
    ctx.fillRect(cherry[0], cherry[1], 10, 10);
    ctx.fillStyle = 'black';
    for (let block of body) {
        ctx.fillRect(block[0], block[1], 10, 10);
    }
}, 200);

setInterval(function () {
    cherry[0] = Math.random() * 500;
    cherry[1] = Math.random() * 500;
}, 20000);

document.addEventListener('keydown', function (event) {
    switch (event.key) {
        case 'ArrowRight':
            dir = [10, 0];
            break;
        case 'ArrowLeft':
            dir = [-10, 0];
            break;
        case 'ArrowUp':
            dir = [0, -10];
            break;
        case 'ArrowDown':
            dir = [0, 10];
            break;
    }
})
