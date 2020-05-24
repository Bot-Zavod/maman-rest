window.onload = function() {
    var coll = document.getElementsByClassName("collapsible");
    var i;

    for (i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function() {
        this.classList.toggle("active")
        var content = this.nextElementSibling;
        if (content.style.maxHeight === 0+"px"){
            /*this.classList.remove("disactive");
            this.classList.add("active");*/
            content.style.maxHeight = content.scrollHeight + "px";
        } else {
            /*this.classList.remove("active");
            this.classList.add("disactive");*/
            content.style.maxHeight = 0+"px";
        }
      });
    }
}


function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


window.smoothScroll = async function(target) {
    await sleep(1000);
    var scrollContainer = target;
    do { //find scroll container
        scrollContainer = scrollContainer.parentNode;
        if (!scrollContainer) return;
        scrollContainer.scrollTop += 1;
    } while (scrollContainer.scrollTop == 0);

    var targetY = 30;
    do { //find the top of target relatively to the container
        if (target == scrollContainer) break;
        targetY += target.offsetTop;
    } while (target = target.offsetParent);

    scroll = function(c, a, b, i) {
            i++;
            if (i > 30) return;
            c.scrollTop = a + (b - a) / 30 * i;
            setTimeout(function() { scroll(c, a, b, i); }, 6);
        }
        // start scrolling
        // console.log(scrollContainer, scrollContainer.scrollTop, targetY, 0)
    scroll(scrollContainer, scrollContainer.scrollTop, targetY - 100, 0);
}

//Get the button:
mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() { scrollFunction() };

function scrollFunction() {
    var treshhold = 600;
    if (document.body.scrollTop > treshhold || document.documentElement.scrollTop > treshhold) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}