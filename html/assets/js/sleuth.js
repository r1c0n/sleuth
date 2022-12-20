document.getElementById("sleuthForm").addEventListener("submit", function(event) {
    event.preventDefault();  // Prevent form from being submitted
  
    // Get the user's input
    var user = document.getElementById("user").value;
  
    // Display the links
    document.getElementById("output").innerHTML = "this will be finished soon"
  });
  