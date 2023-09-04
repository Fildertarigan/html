function spin() {
    var spinner = document.getElementById('spinner');
    
    spinner.classList.add('spin-animation');
    
    setTimeout(function() {
      spinner.classList.remove('spin-animation');
      showResult();
    }, 2000);
  }
  
  function showResult() {
    var result = Math.floor(Math.random() * 100) + 1;
  
    if (result <= 10) {
      alert("Congratulations! You won the rare item!");
    } else if (result <= 30) {
      alert("Congratulations! You won the uncommon item!");
    } else {
      alert("You won the common item. Better luck next time!");
    }
  }
  