document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded')

    heart = document.querySelectorAll('#heart')
    heart.forEach(element => {
        element.addEventListener("click", function(){
            const countdiv = element.parentElement;
            const postdiv = countdiv.parentElement;
            const thevalue = postdiv.querySelector(".thevalue").getAttribute("data-value")
            let currentcount = countdiv.querySelector(".counting").innerHTML
            console.log(currentcount)
            fetch('/likepost/' + thevalue, {
                method: 'POST',
                body: JSON.stringify({
                     post : thevalue
                })
              })
            .then(response => response.json())
            .then(result => {
                console.log(result);
            })
            
            if (element.className === "fa fa-heart red-color"){
                element.className = "fa fa-heart-o";
                currentcount--
                console.log(currentcount)
                countdiv.querySelector(".counting").innerHTML = currentcount
            }
            else{
                element.className = "fa fa-heart red-color"
                currentcount++
                console.log(currentcount)
                countdiv.querySelector(".counting").innerHTML = currentcount
            }
            return false
            
        })
    })
    
    button = document.querySelectorAll('.edit')
    button.forEach(element => {
        element.addEventListener("click", function(){
            const parent = element.parentElement;
            // get value of post id
            const thevalue = parent.querySelector(".thevalue").getAttribute("data-value")
            // find correct divs
            const content = parent.querySelector("#content")
            const edittext = parent.querySelector("#edittext")
            // get existing post content
            post = parent.querySelector(".content").innerHTML
            // hide and show correct divs
            content.style.display = "none";
            edittext.style.display = "block";
            element.style.display = "none"
            // add content to new text area.
            newtext = parent.querySelector(".edittext")
            newtext.value = post
            // get save button
            save = parent.querySelector(".save")
            // add eventlistener to save button
            save.addEventListener('click', function(){
                fetch('/editpost/' + thevalue, {
                    method: 'POST',
                    body: JSON.stringify({
                        post: newtext.value,
                    })
                  })
                .then(response => response.json())
                .then(result => {
                    console.log(result);
                })
                .then(
                // revert back to orignal view with new post
                content.style.display = "block",
                edittext.style.display = "none",
                element.style.display = "inline",
                parent.querySelector(".content").innerHTML = newtext.value,
                )
            })
            return false;
        })  
        return false;
    })
    return false;
})
