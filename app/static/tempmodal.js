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

  var viewJobButtons = document.querySelectorAll("#jobsTable .view-btn");
  viewJobButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      var row = button.closest("tr");
      var cells = row.querySelectorAll("td");
      document.getElementById("viewRequest").value = cells[0].textContent;
      document.getElementById("viewUser").value = cells[1].textContent;
      document.getElementById("viewPay").value = cells[2].textContent;
      document.getElementById("viewLocation").value = cells[3].textContent;
      document.getElementById("viewTimeFrame").value = cells[4].textContent;
      document.getElementById("viewStatus").value = cells[5].textContent;
      var viewJobModal = new bootstrap.Modal(document.getElementById("viewJobModal"), {});
      viewJobModal.show();
    });
  });


    // View button click event for the applications table
  var viewApplicationButtons = document.querySelectorAll("#hireMeTable .view-btn");
  viewApplicationButtons.forEach(function (button) {
    button.addEventListener("click", function () {
     var row = button.closest("tr");
     var cells = row.querySelectorAll("td");
     document.getElementById("viewService").value = cells[0].textContent;
     document.getElementById("viewProvider").value = cells[1].textContent;
     document.getElementById("viewDetails").value = cells[2].textContent;
     document.getElementById("viewExperience").value = cells[3].textContent;
     document.getElementById("viewAvailability").value = cells[4].textContent;
     document.getElementById("viewContactInfo").value = cells[5].textContent;
     var viewApplicationModal = new bootstrap.Modal(document.getElementById("viewApplicationModal"), {});
     viewApplicationModal.show();
   });
  });
