import React, { Component } from 'react';
import './App.css';
import { Container, Row, Col } from 'reactstrap';
import createClass from 'create-react-class';


var NumberSquare = createClass({
    render: function (){
        var w = '100%';
        var h = 200;
        var dataset = [{'num_tweet':100, 'num_hash':30, 'num_utenti':15}];

	    return (<svg width={w} height={h} className='NumSquare'>
	                <RectText />
	            </svg>)
    }
});

// Gruppo per testo e rettangolo
var RectText = createClass({

    render: function (){

       var translate = "translate(0,30)"
       return(<g transform={translate}>
                <rect width="200" height="200"></rect>
              </g>
              )
    }

});

// Rettangolo
var Rectangle = createClass({

    render: function (){
        return (<h1>ciao</h1>)
    }

});


// Testo
var Text = createClass({

    render: function(){
        return (<h1>ciao</h1>)
    }

});


export default NumberSquare;