
const form_value_select = document.getElementById("form_select")

form_value_select.onclick = changeFormType(form_value_select.value)

function changeFormType(form_value_select.value){
    var tmp = document.getElementById("form_select");
    if(form_value_select.value != tmp.value){
        location.reload()
    }
}
