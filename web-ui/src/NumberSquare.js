import React, { Component } from 'react';
import './App.css';
import { Container, Row, Col } from 'reactstrap';
import createClass from 'create-react-class';
import { select } from 'd3-selection';
import { VictoryBar } from 'victory';



var NumberSquare = createClass({



    //componentWillMount: function (){

    //},



    render: function (){
        var w = '100%';
        var h = 200;
        //var dataset = [{'num_tweet':100, 'num_hash':30, 'num_utenti':15}];
        var dataSet = [{'num_tweet':100, 'num_hash':30, 'num_utenti':15}]

	    return (
	                <VictoryBar />
	                //<RectText data={dataSet}/>
	            )
    }
});

// Gruppo per testo e rettangolo
var RectText = createClass({

    //componentWillMount: function (){
        //this.rectWidth = "100%";
        //this.rectHeight = "100%";
        //this.rectangle =  select()

    //    this.update_d3(this.props);
    //},

    //componentWillReceiveProps: function (newProps){
    //    this.update_d3(newProps);
    //},

     //componentDidUpdate: function() {
	 //  this.update_d3({data: this.props.data});
     //   },


    componentDiDMount: function (props) {
        var node = this.node;



        select(node).selectAll('rect-sidebar-tweet')
                     .data(this.props.data)
                     .enter()
                     .append('rect')
                     .attr("rx", 4)
                     .attr("width", '100%')
                     .attr("height", "100%")
                     .attr('fill', '#66a3ff');
    },

    render: function (){

       var translate = "translate(0,30)"
       return(<svg ref={node => this.node = node} width='100%' height='200'>
              </svg>
              )
    }

});

// Rettangolo
var Rectangle = createClass({

    render: function (){
        return (<Text />)
    }

});


// Testo
var Text = createClass({

    render: function(){
        return (<h1 style="color: white;">ciao</h1>)
    }

});


export default NumberSquare;