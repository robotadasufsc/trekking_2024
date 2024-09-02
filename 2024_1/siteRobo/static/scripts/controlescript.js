function stop_car() { 
    fetch('/stop-car') 
      .then(response => response.json()) 
      .then(data => console.log(data)) 
      .catch(error => console.error(error)); 
  }
function move_forward_car() { 
    fetch('/move-forward-car') 
      .then(response => response.json()) 
      .then(data => console.log(data)) 
      .catch(error => console.error(error)); 
}
function move_backward_car() { 
    fetch('/move-backward-car') 
      .then(response => response.json()) 
      .then(data => console.log(data)) 
      .catch(error => console.error(error)); 
}
function move_left_car() { 
    fetch('/move-left-car') 
      .then(response => response.json()) 
      .then(data => console.log(data)) 
      .catch(error => console.error(error)); 
}
function move_right_car() { 
    fetch('/move-right-car') 
      .then(response => response.json()) 
      .then(data => console.log(data)) 
      .catch(error => console.error(error)); 
}