document.addEventListener('DOMContentLoaded', function () {
  console.log('Doctors script loaded successfully');

  // Get references to the department and doctor dropdowns
  const departmentDropdown = document.getElementById('id_department');
  const doctorDropdown = document.getElementById('id_doctor');

  // Add event listener to the department dropdown
  departmentDropdown.addEventListener('change', function () {
    const departmentId = this.value; // Get the selected department ID

    if (departmentId) {
      // Fetch doctors based on the selected department
      fetch(`/ajax/load-doctors/?department_id=${departmentId}`)
        .then(response => response.json())
        .then(data => {
          // Clear the doctor dropdown
          doctorDropdown.innerHTML = '';

          // Populate the doctor dropdown with the retrieved data
          data.forEach(doctor => {
            const option = document.createElement('option');
            option.value = doctor.id;
            option.textContent = doctor.name;
            doctorDropdown.appendChild(option);
          });
        })
        .catch(error => {
          console.error('Error loading doctors:', error);
        });
    } else {
      // Clear the doctor dropdown if no department is selected
      doctorDropdown.innerHTML = '';
    }
  });
});
