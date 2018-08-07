// 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
const sgMail = require('@sendgrid/mail');
sgMail.setApiKey(process.env.SENDGRID_API_KEY);
// const msg = {
//   to: 'cz284@cornell.edu',
//   cc: 'catherinekzhou@gmail.com',
//   from: 'catherinekzhou@gmail.com',
//   subject: 'Test',
//   text: 'What would you like to know?',
//   html: '<form>First name:<br><input type="text" name="firstname"><br>Last name:<br><input type="text" name="lastname"><br><input type="submit" value="Submit"></form>',
// };

const msg = {
  "personalizations": [
    {
      "to": [
        {
          "email": "cz284@cornell.edu"
        }
      ],
      "subject": "Hello, World!"
    }
  ],
  "from": {
    "email": "catherinekzhou@gmail.com"
  },
  "content": [
    {
      "type": "text/plain",
      "value": "Hello, World!"
    }
  ]
}
sgMail.send(msg);
