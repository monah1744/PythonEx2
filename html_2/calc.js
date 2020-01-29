let $output = document.getElementById('output');


document.querySelector('.card-body').addEventListener('click', function (event) {
    if (event.target.classList.contains('btn-primary')) {
        $output.innerHTML += ' ' + event.target.innerHTML;
    }
});
