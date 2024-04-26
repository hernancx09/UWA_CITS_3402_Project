document.addEventListener("DOMContentLoaded", function () {
    // Edit button click event for the ongoing jobs table
    var editJobButtons = document.querySelectorAll("#jobsTable .edit-btn");
    editJobButtons.forEach(function (button) {
      button.addEventListener("click", function () {
        var row = button.closest("tr");
        var cells = row.querySelectorAll("td");
        document.getElementById("editRequest").value = cells[0].textContent;
        document.getElementById("editUser").value = cells[1].textContent;
        document.getElementById("editPay").value = cells[2].textContent;
        document.getElementById("editLocation").value = cells[3].textContent;
        document.getElementById("editTimeFrame").value = cells[4].textContent;
        document.getElementById("editStatus").value = cells[5].textContent;
        var editJobModal = new bootstrap.Modal(document.getElementById("editJobModal"), {});
        editJobModal.show();
      });
    });

    // Edit button click event for the applications table
    var editApplicationButtons = document.querySelectorAll("#hireMeTable .edit-btn");
    editApplicationButtons.forEach(function (button) {
      button.addEventListener("click", function () {
        var row = button.closest("tr");
        var cells = row.querySelectorAll("td");
        document.getElementById("editService").value = cells[0].textContent;
        document.getElementById("editProvider").value = cells[1].textContent;
        document.getElementById("editDetails").value = cells[2].textContent;
        document.getElementById("editExperience").value = cells[3].textContent;
        document.getElementById("editAvailability").value = cells[4].textContent;
        document.getElementById("editContactInfo").value = cells[5].textContent;
        var editApplicationModal = new bootstrap.Modal(document.getElementById("editApplicationModal"), {});
        editApplicationModal.show();
      });
    });
  });