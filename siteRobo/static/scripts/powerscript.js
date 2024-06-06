function move_forward() { 
    fetch('/move-forward') 
      .then(response => response.json()) 
      .then(data => console.log(data)) 
      .catch(error => console.error(error)); 
  } 