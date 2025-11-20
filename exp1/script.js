function showMsg(msg, ok=true){
  const el = document.getElementById('confirmation');
  el.textContent = msg; el.style.color = ok ? 'green' : 'red';
}
document.getElementById('btn').addEventListener('click', function(){
  const f = id => document.getElementById(id).value.trim();
  const first = f('first'), last = f('last'), email = f('email'),
        mobile = f('mobile'), gender = f('gender'),
        pass = f('password'), repass = f('repassword');
  if(!first||!last||!email||!mobile||!gender||!pass||!repass){
    return showMsg('Please fill all fields.', false);
  }
  if(pass !== repass) return showMsg('Passwords do not match!', false);
  // basic mobile numeric check
  if(!/^\d{10}$/.test(mobile)) return showMsg('Enter 10 digit contact.', false);
  // success
  console.log('Registered:', {first,last,email,mobile,gender});
  showMsg(`Thank you, ${first}! Registration successful.`);
});
