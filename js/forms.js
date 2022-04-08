
  // VGS Collect form initialization
  const form = VGSCollect.create("tnte6doqz8w", "sandbox", function(state) {});
  // Create VGS Collect field for credit card name
  form.field("#cc-name", {
    type: "text",
    name: "card_name",
    placeholder: "Joe Business",
    validations: ["required"],
  });

  // Create VGS Collect field for credit card number
  form.field("#cc-number", {
    type: "card-number",
    name: "card_number",
    successColor: "#4F8A10",
    errorColor: "#D8000C",
    placeholder: "4111 1111 1111 1111",
    validations: ["required", "validCardNumber"],
  });

  // Create VGS Collect field for CVC
  form.field("#cc-cvc", {
    type: "card-security-code",
    name: "card_cvc",
    placeholder: "344",
    validations: ["required", "validCardSecurityCode"],
  });

  // Create VGS Collect field for credit card expiration date
  form.field("#cc-expiration-date", {
    type: "card-expiration-date",
    name: "card_expirationDate",
    placeholder: "01 / 2022",
    validations: ["required", "validCardExpirationDate"],
  });

  // Submits all of the form fields by executing a POST request.
  document.getElementById("cc-form").addEventListener(
    "submit",
    function (e) {
      e.preventDefault();
      form.submit("/post", {}, function (status, data) {
        document.getElementById("result").innerHTML = JSON.stringify(
          data.json,
          null,
          4
        );
      });
    },
    function (errors) {
      document.getElementById("result").innerHTML = errors;
    }
  );
