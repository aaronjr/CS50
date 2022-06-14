document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);


  // By default, load the inbox
  load_mailbox('inbox');

  // send email
  document.querySelector("#compose-form").onsubmit = function() {
    // works console.log(document.querySelector('#compose-recipients').value)
    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
          recipients: document.querySelector('#compose-recipients').value,
          subject: document.querySelector('#compose-subject').value,
          body: document.querySelector('#compose-body').value
      })
    })
    .then(response => response.json())
    .then(result => {
        // Print result
        console.log(result);
    });
    
    load_mailbox('sent')
    return false;
  }
  
});

function compose_email() {
  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#individual-view').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function reply_email(sender, subject, body, time){
  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#individual-view').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = sender;
  if (subject.substring(0,3) == "RE:"){
    document.querySelector('#compose-subject').value = subject;
  }
  else{
    document.querySelector('#compose-subject').value = "RE: " + subject;
  }
  document.querySelector('#compose-body').value = 'On ' + time + ', ' + sender + ' wrote ' + body + ' \n' + '\n';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#individual-view').style.display = 'none';

  fetch('/emails/' + mailbox)
  .then(response => response.json())
  .then(emails => {
      //Loop through emails and add to page
      emails.forEach(emails => {    
        console.log(emails) 
        // create div
        const eachemail = document.createElement('div');
        // add class
        eachemail.className += "eachemail";
        // change color accordingly
        if (emails.read === true){
          eachemail.style.backgroundColor = "rgb(224, 223, 223)";
        }
        else{
          eachemail.style.backgroundColor = "white";
        }
        // create items
        const sender = document.createElement('h5');        
        const emailsubject = document.createElement('h7');
        const time = document.createElement('p');
       
        // set innerHTMLs
        sender.innerHTML = emails.sender;
        emailsubject.innerHTML = emails.subject;
        time.innerHTML = emails.timestamp;
        
        // add div to email view
        document.querySelector('#emails-view').appendChild(eachemail);

        // add items into div
        eachemail.appendChild(sender);
        eachemail.appendChild(emailsubject);
        eachemail.appendChild(time);

        // load the full email when clicking on a preview
        eachemail.onclick = function(){
          // Show the mailbox and hide other views
          document.querySelector('#emails-view').style.display = 'none';
          document.querySelector('#compose-view').style.display = 'none';
          document.querySelector('#individual-view').style.display = 'block';

          // Clear children items from individual-view to stop them stacking
          let parent = document.querySelector('#individual-view');
          while (parent.firstChild) {
            parent.removeChild(parent.firstChild);
          }

          // get actual email
          fetch('/emails/' + emails.id)
          .then(response => response.json())
          .then(emails => {

              fetch('/emails/' + emails.id, {
                method: 'PUT',
                body: JSON.stringify({
                    read: true
                })
              })

              // create div
              const wholeemail = document.createElement('div');
              wholeemail.className += "wholeemail";

              // create items
              const sender = document.createElement('h5');    
              const recipients = document.createElement('h5')    
              const emailsubject = document.createElement('h7');
              const body = document.createElement('p');
              const time = document.createElement('p');
            
              // set innerHTMLs
              sender.innerHTML = "Sent by: " + emails.sender;
              recipients.innerHTML = "Recepients: " + emails.recipients
              emailsubject.innerHTML = "Subject: " + emails.subject;
              time.innerHTML = "Sent at: " + emails.timestamp;
              body.innerHTML = emails.body;
              
              // add div to email view
              document.querySelector('#individual-view').appendChild(wholeemail);

              // add items into div
              wholeemail.appendChild(sender);
              wholeemail.appendChild(recipients);
              wholeemail.appendChild(emailsubject);
              wholeemail.appendChild(body);
              wholeemail.appendChild(time);
              
              // add reply and archive buttons if they arent the sender
              if(document.getElementById('#user').innerHTML !== emails.sender){
                if(emails.archived === true){
                  const btn = document.createElement('button');
                  btn.innerHTML = "Unarchive";
                  btn.className += "btn btn-primary"
                  wholeemail.appendChild(btn);
                  // unarchive email
                  btn.addEventListener('click', function() {
                    fetch('/emails/' + emails.id, {
                      method: 'PUT',
                      body: JSON.stringify({
                          archived: false
                      })
                    })
                    window.location.reload();
                    return false;
                  }) 
                  // console.log(emails.archived)
                }
                else{
                  // create button to archive email
                  const btn = document.createElement('button')
                  btn.innerHTML = "Archive";
                  btn.className += "btn btn-primary"
                  wholeemail.appendChild(btn);
                  btn.addEventListener('click', function() {
                    fetch('/emails/' + emails.id, {
                      method: 'PUT',
                      body: JSON.stringify({
                          archived: true
                      })
                    })
                    window.location.reload();
                    return false;
                    })
                  }
                // create button to reply - not if they sent  
                let btn = document.createElement('button');
                btn.innerHTML = "Reply";
                btn.className += "btn btn-primary"
                wholeemail.appendChild(btn);
                btn.addEventListener('click', function() { 
                  reply_email(
                    emails.sender, 
                    emails.subject, 
                    emails.body, 
                    emails.timestamp);
                })
              }
            }
          )}
        }
      )
    })
  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = 
    `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

    return false;
}
