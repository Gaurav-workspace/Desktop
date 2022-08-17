window.onload = function(params) {
    console.log(89);
    let angle1 = 0;
    let angle2=120;
    let angle3=240;
    
    setInterval(()=>{
        document.querySelector('.rod1').style.transform = `rotate(${angle1}deg)`;
        document.querySelector('.rod2').style.transform = `rotate(${angle2}deg)`;
        document.querySelector('.rod3').style.transform = `rotate(${angle3}deg)`;
        angle1+=1;
        angle1%=360;
        angle2+=1;
        angle2%=360;
        angle3+=1;
        angle3%=360;
    },50)
    
    
}