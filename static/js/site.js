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

let reservationEventInput = document.getElementById('reservation-event'),
    inputStartDate = document.getElementById('start-date'),
    inputStartTime = document.getElementById('start-time');

const getReservationTimes = () => {
    let eventId = reservationEventInput.value,
        date = inputStartDate.value,
        url = `/reservations/get_reservation_times/${eventId}?date=${date}`;

    fetch(url)
        .then((response) => response.json())
        .then((response) => {
            inputStartTime.innerHTML = '';

            let fragment = document.createDocumentFragment();

            response.data.forEach((time) => {
                let optionElement = document.createElement('option');
                optionElement.setAttribute('value', time);
                optionElement.textContent = time.split('T')[1];

                fragment.appendChild(optionElement);
            });

            inputStartTime.appendChild(fragment);
        });
};

if (inputStartDate != null && inputStartDate != undefined) {
    let currentDate = new Date();

    if (inputStartDate.value === '') {
        inputStartDate.value = currentDate.toISOString().split('T')[0];
    }

    inputStartDate.addEventListener('change', () => getReservationTimes());
}

if (inputStartTime != null && inputStartTime != undefined) {
    getReservationTimes();
}
