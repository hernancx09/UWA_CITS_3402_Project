
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
async function clicked(job_id, employer_id) {
  await sleep(1000);
  document.getElementById("job_id").value = job_id;
  document.getElementById("employer_id").value = employer_id;
}

var viewJobButtons = document.querySelectorAll(".apply-btn");
viewJobButtons.forEach(function (button) {
  button.addEventListener("click", function () {
    var viewJobModal = new bootstrap.Modal(document.getElementById("viewJobModal"), {});
    viewJobModal.show();
  });
});

