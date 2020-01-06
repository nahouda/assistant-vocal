'use strict';

// ------------------------------------------------------------------
// APP INITIALIZATION
// ------------------------------------------------------------------

const { App } = require('jovo-framework');
const { Alexa } = require('jovo-platform-alexa');
const { GoogleAssistant } = require('jovo-platform-googleassistant');
const { JovoDebugger } = require('jovo-plugin-debugger');


const { FileDb } = require('jovo-db-filedb');
const app = new App();



var list =[];
var id =[];
app.use(
    new Alexa(),
    new GoogleAssistant(),
    new JovoDebugger(),
    new FileDb(),
);
// Requete HTTP
var HttpClient = function() {
    this.get = function(aUrl, aCallback) {
        var anHttpRequest = new XMLHttpRequest();
        anHttpRequest.onreadystatechange = function() { 
            if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200)
                aCallback(anHttpRequest.responseText);
        }

        anHttpRequest.open( "GET", aUrl, true );            
        anHttpRequest.send( null );
    }
}

// ------------------------------------------------------------------
// APP LOGIC
// ------------------------------------------------------------------

app.setHandler({
    LAUNCH() {
        return this.toIntent('HelloIntent');
    },
     HelloIntent() {
        this.ask('Welcome to Near Me Alexa application ! we help you find your destination  near by and connect with them. ','I dont know if you heard me, welcome to your custom alexa application!');
    },

     SearchForIntent() {
      
      
       
       var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
       var xhr = new XMLHttpRequest();
       xhr.open('GET', "https://api.ipgeolocation.io/ipgeo?apiKey=6798734ccaa444cdbebfb4c38e3f0d90",false);
       xhr.send();
       var response = JSON.parse(xhr.responseText);
       var location=response;
       xhr.open('GET', "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+location.latitude+","+location.longitude+"&rankby=distance&type="+this.$inputs.type.value+"&key=AIzaSyCzwnTnE1ZTYwn31SMA24xAS7iNjDN2BT4", false);
      
       xhr.send();
       var response = JSON.parse(xhr.responseText);
       console.log(JSON.stringify(response));
       
       
   
       
        for (var i in response.results) {
           // if(response.results[i].name == this.$input.type.value)
            //{response.results[i].place_id  }
            //console.log(abbad_id); 
            list[i]  = response.results[i].name;
            id[i]= response.results[i].place_id;
           
   
        }
     this.ask('We found the following  '+ this.$inputs.type.value +'s.' + list + '. Which one do you prefer to go?' ); 
        
    },
  /*  MyChoiceIntent() {
       var j  ;
        for (var i = 0 ; i < list.length; i++) { 
            if( list[i] ===this.$inputs.name.value)   {  j=id[i] }
            }
           console.log(j);
           
    var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
    var xhr = new XMLHttpRequest();
      xhr.open('GET', "https://maps.googleapis.com/maps/api/place/details/json?placeid=ChIJ1Rk99IY0_RIRJx7OI8WVj4c&fields=name,rating,formatted_phone_number&key=AIzaSyCzwnTnE1ZTYwn31SMA24xAS7iNjDN2BT4", false); 
      xhr.send();
      var response = JSON.parse(xhr.responseText);
      console.log(JSON.stringify(response));
    
     
         this.ask('For more information about ' + this.$inputs.name.value +  ' you can call phone number ' + response.result.formatted_phone_number + '.' ); 

    },*/
});


module.exports.app = app;


