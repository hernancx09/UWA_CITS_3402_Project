
const form_select = document.getElementById("post_type")
const POST_JOB = "Job request"

const form_job_name = document.getElementById("job_name_wrapper")
const form_pay = document.getElementById("pay_wrapper")
const form_date = document.getElementById("start_from_date_wrapper")
const form_status= document.getElementById("status_wrapper")
const form_looking_for = document.getElementById("looking_for_wrapper")

setVisibility(form_looking_for, 0)

form_select.addEventListener("change", changeFormType)

function setVisibility(element, int){
    if(int == 0){
        element.style.visibility = "hidden"
        element.style.display = "none"
    } else {
        element.style.display = "block"
        element.style.visibility = "visible"
    }

}
function changeFormType(){
    if(form_select.value != POST_JOB){
        setVisibility(form_job_name, 0)
        setVisibility(form_looking_for, 1)
        setVisibility(form_pay, 0)
        setVisibility(form_date, 0)
        setVisibility(form_status, 0)
    } else {
        setVisibility(form_job_name, 1)
        setVisibility(form_looking_for, 0)
        setVisibility(form_pay, 1)
        setVisibility(form_date, 1)
        setVisibility(form_status, 1)
    }
}
