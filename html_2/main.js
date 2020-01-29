

// let console1 = document.getElementById('console');

// console.log(console1);

// console1.innerHTML = 'lorem';

// let form = document.getElementById("form1")

// console.log(form);

let $cards = document.getElementById("cards")
let $counter = document.getElementById("counter");

console.log($counter);

$counter.innerHTML = 2

document.body.addEventListener("click", function (event) {
    if (event.target.classList.contains("btn-primary")) {
        console.log(event);
        $counter.innerHTML = Number($counter.innerHTML) + 1;
    }
});

for (let i = 1; i <= 10; i++) {
    $cards.innerHTML = 
}
