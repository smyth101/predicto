


function show_account_options(){

    var profile = document.getElementById("profile_options");
    if(profile.style.display == "block"){
        profile.style.display = "none";
    }
    else{
        profile.style.display = "block";
    }
    window.addEventListener('mouseup',function(event){
        var dropdown = document.getElementById('profile_options');
        if(event.target != dropdown && event.target.parentNode != dropdown){
            dropdown.style.display = 'none';
        }
    });
    
    
}

function show_signout(){
    var signout = document.getElementById("signout");
    signout.style.display = "block";

    window.addEventListener('mouseup',function(event){
        var signout = document.getElementById('signout');
        if(event.target != signout && event.target.parentNode != signout){
            signout.style.display = 'none';
        }
    });
   
    // document.onclick = function(e){
    //     if(e.target.id !== "signout"){
    //         signout.style.display = "none";
    //     }
    // }
}



function cancel_signout(){
    var signout = document.getElementById("signout");
    signout.style.display = "none";

}

function overall_scores(){
    // window.onload = function(){
        var value_array = document.getElementsByName('game_score');
        var total = 0
    for(var i=0;i< value_array.length;i++){
        total = total + parseInt(value_array[i].innerHTML); 
    

    console.log(value_array[i].innerHTML);
    }
    console.log(total);
    document.getElementById('user_score_container').innerHTML =document.getElementById('user_score_container').innerHTML + total;
    value_array = document.getElementsByName('site_game_score');
        total = 0
    for(var i=0;i< value_array.length;i++){
        total = total + parseInt(value_array[i].innerHTML); 
    

    console.log(value_array[i].innerHTML);
    }
    console.log(total);
    document.getElementById('site_score_container').innerHTML =document.getElementById('site_score_container').innerHTML + total;
    
// }
}




function scroll_down(){
    var headerHeight = document.getElementById("header").clientHeight;
    var navHeight = document.getElementById("nav_bar").clientHeight;
    var contentHeight = document.getElementById("content_container").clientHeight;

    var scroll_height = headerHeight + navHeight + contentHeight;
    console.log(headerHeight);
    console.log(navHeight);
    console.log(contentHeight);
    console.log(scroll_height);
    window.onload = function(){scrollBy(0,scroll_height);}
}