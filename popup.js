var url;
chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function
(tabs) {
    url = tabs[0].url;
    // document.getElement
    // ById("host").innerHTML = url;
    // document.getElementById("host2").value = url;
});
window.onload= function (){
        let language = "fr"
        const option1 = document.getElementById("option1");
        const option2 = document.getElementById("option2");
        const slider = document.getElementById("range");
        option1.addEventListener("click", (event) => {
            language = "fr";
        });
        option2.addEventListener("click", (event) => {
            language = "en"
        });
        const submit = document.getElementById("summarize");
        submit.addEventListener("click", (event) => {
        var newxmlhttp = new XMLHttpRequest();
        var theUrl = "http://127.0.0.1:8000/results";
        newxmlhttp.open("POST", theUrl, true);
        newxmlhttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=UTF-8");
        newxmlhttp.send("url="+url+"&language="+language+"&slider="+slider.value);
        newxmlhttp.onreadystatechange = function() {
            if (newxmlhttp.readyState == 4){
                // alert(newxmlhttp.responseText));
                const parsed = JSON.parse(newxmlhttp.responseText); // an *array* that contains the user
                // alert(parsed.resume);
                // document.write(parsed.resume);
                document.getElementById("text_resume").innerHTML= parsed.resume;
            }
        };
    });
};
