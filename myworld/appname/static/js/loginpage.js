function valid()
{
  var md=document.getElementById("mid").value;
  var rmd=/^[a-zA-z 0-9]+[@][a-z]+[\.][a-z]{2,3}$/;
  var pwd=document.getElementById("password").value;
  var rp=/[a-zA-Z 0-9\@\.\-\_\#]{8}$/;
  
  if((md=="")||(pwd==""))
  {
    alert("not empty");
  }
  else
  {
   if(rmd.test(md) && rp.test(pwd))
    {
      alert("successful login");
    }
    else
    {
      alert("enter the valid details");
    }

  }
  }