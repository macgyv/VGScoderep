# simple_app_test_vgs


VGS injest any type of data securely and forward that sensitive data it's reverse proxy then aliased that data, now the aliased data forwards to merchants server then transfer to VGS Forward proxy going to issuing bank/target host.

To configure this scenario, after registering a VGS account, you need to configure the INBOUND connection, add the upstream (merchant API Server) or in this case, is the VGS echo server (https://echo.apps.verygood.systems) in place with the client server, add the fields for REDACT like in this case

$.card_holder
$.card_number
$.card_cvc
$.card_exp

Same with the OUTBOUND, though the OUTBOUND (https://echo.apps.verygood.systems) should route to a payment gateway like STRIPE for integration

also make a note of your VAULT ID and Access Credential account for later use.

===Preparing html and scripts===
VGS has a form designer where you can create your custom form with all the required script on it, from this assignment I use the credit-card-example.html.

from the code, you need to add the VGS-collect.js javascript library by adding this line to your HTML code


<script type="text/javascript" src="https://js.verygoodvault.com/vgs-collect/2.12.0/vgs-collect.js"></script>


create a form with submit button and then initialize the form using the VGS Collect library adding the VAULT ID and evironment as shown below

const form = VGSCollect.create("<VAULT ID>", "<ENVIRONMENT>", function(state) {});

const form = VGSCollect.create("tnte6doqz8w", "sandbox", function(state) {});

then create a VGS Collect field from the instantiated form object for all your fields that you want to pass to VGS reverse proxy


form.field("#cc-name", {
        type: "text",
        name: "card_name",
        placeholder: "Joe Business",
        validations: ["required"],
      });


and at submit form, invoke the submit method to send a POST requests

form.submit("/post", {}, function (status, data)


This will submits all the form fields by executing a POST request to your VGS account that will be hitting the VGS INBOUND ROUTE then REDACT and the ECHO UPSTREAM will reply in JSON format, though in live scenario, this will hit the merchants server with redacted data.

Then the merchants server will forward that data (some fields are aliased depending on the configuration) going to VGS Forward Proxy (OUTBOUND) (example for live is api.stripe.com but in the demo still using the VGS Echo server) and convert from aliased to real data going to bank/target host using the VGS INTEGRATION.

In this way, there's no sensitive data stored at merchant's server.

**unfortunately when I select the INTIGRATION LINK it give's me an error, anyways, I'm amazed with superb documentation and community that VGS team provides, it's a bit overwhelm but amazing, kudos to VGS Team :).
