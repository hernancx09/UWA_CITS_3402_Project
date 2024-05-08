
const form_select = document.getElementById("post_type")
const POST_JOB = "Job request"

const form_name = document.getElementById("name-label")
const form_pay = document.getElementById("pay_wrapper")
const form_date = document.getElementById("start_from_date_wrapper")
const form_status= document.getElementById("status_wrapper")

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
        form_name.innerHTML = "Looking For"
        setVisibility(form_pay, 0)
        setVisibility(form_date, 0)
        setVisibility(form_status, 0)
    } else {
        form_name.innerHTML = "Job Name"
        setVisibility(form_pay, 1)
        setVisibility(form_date, 1)
        setVisibility(form_status, 1)
    }
}
