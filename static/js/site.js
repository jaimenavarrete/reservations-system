/**
 * ****************************************************************************
 * RESERVA24 CODE
 * ****************************************************************************
 */

/**
 * Delete Confirmation Modal Dialog
 */

let deleteElementBtns = document.querySelectorAll('.delete-element-btn');

deleteElementBtns.forEach((btn) =>
    btn.addEventListener('submit', (e) => {
        e.preventDefault();

        Swal.fire({
            title: 'Are you sure?',
            text: "You won't be able to revert this!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Yes, delete it!',
        }).then((result) => {
            if (result.isConfirmed) {
                btn.submit();
            }
        });
    })
);

/**
 * Copy event link button
 */

let copyLinkBtns = document.querySelectorAll('.copy-link-btn');

copyLinkBtns.forEach((btn) => {
    btn.addEventListener('click', async (e) => {
        e.preventDefault();

        await navigator.clipboard.writeText(btn.href);

        btn.classList.add('text-success');
        btn.innerHTML = '<i class="bi bi-check-lg"></i> Copied!';

        setTimeout(() => {
            btn.innerHTML = '<i class="bi bi-clipboard-fill"></i> Copy link';
            btn.classList.remove('text-success');
        }, 1500);
    });
});

/**
 * Change event state button
 */

let changeStateBtns = document.querySelectorAll('.change-state-btn');

changeStateBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
        let checkInput = btn.querySelector('.form-check-input');
        checkInput.click();

        btn.submit();
    });
});

/**
 * Get the reservations times and insert them to the reservation time select
 */

let inputStartDate = document.getElementById('start-date');
let inputStartTime = document.getElementById('start-time');

if (inputStartDate != null && inputStartDate != undefined) {
    let currentDate = new Date();

    if (inputStartDate.value === '') {
        inputStartDate.value = currentDate.toISOString().split('T')[0];
    }
}

if (inputStartTime != null && inputStartTime != undefined) {
    fetch('/reservations/get_reservation_times/')
        .then((response) => response.json())
        .then((reservation_times_list) => {
            let fragment = document.createDocumentFragment();

            reservation_times_list.forEach((time) => {
                let optionElement = document.createElement('option');
                optionElement.setAttribute('value', time.value);
                optionElement.textContent = time.name;

                fragment.appendChild(optionElement);
            });

            inputStartTime.appendChild(fragment);
        });
}
