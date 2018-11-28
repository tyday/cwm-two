window.onscroll = function() {scrollFunction()};


function scrollFunction(){
    if (document.body.clientWidth >=600){
        if (document.body.scrollTop > 80 ||
        document.documentElement.scrollTop > 80){
            document.getElementById("headerID").style.height = "50px";
            document.getElementById("logo").style.height = "50px";
            // document.getElementById("nav-links").style.height = "40px";
            // document.getElementById("nav-links").style.padding = "10px 0 0 0";
            // navLinks = document.getElementById("nav-link")
            navLink = document.getElementsByClassName('nav-link');
            for(i=0;i<navLink.length;i++){
                navLink[i].style.padding="15px 0";
            }
            
        }
        else{
            document.getElementById("headerID").style.height = "100px";
            document.getElementById("logo").style.height = "100px";
            // document.getElementById("nav-links").style.height = "60px";
            // document.getElementById("nav-links").style.padding = "40px 0 0 0";
            navLink = document.getElementsByClassName('nav-link');
            for(i=0;i<navLink.length;i++){
                navLink[i].style.padding="40px 0";
            }
        }
    }
}

// function toggleMenu(){
    
    // navLink = document.getElementsByClassName("nav-link");
    // if(navLink[0].offsetParent === null){
    //     for(i=0;i<navLink.length;i++){
    //         navLink[i].style.display="inline";
    //     }
    // } else {
    //     for(i=0;i<navLink.length;i++){
    //         navLink[i].style.display="none"; 

//     }
// }
    // var x = document.getElementById("nav-links");
//     if (x.className === "topnav"){
//         x.className += " toggle";
//         window.addEventListener("click", clickOutsideMenu())
//     } else {
//         x.className = "topnav";
//     }
// }
// function clickOutsideMenu(event){
//     var x = document.getElementById("nav-links");
//     console.log('clicked outside')
//     if (event.target != x && event.target.parentNode != x){
//     if (x.classList.contains('toggle')){
//         console.log('and fired close function')
//         x.className = "topnav"
//     }}
// }