import React, { Component } from 'react';
import createClass from 'create-react-class';
import './App.css';
import listaHash from './data/listaHash.js';


var Topic = createClass({

        render: function (){
            return (<div className='Topic'>
                        <form action="/hello" method="post">

                            <button className='topic-btn' name='selectedTopic' value={this.props.children}>#{this.props.children}</button>
                        </form>
                    </div>);
        }
});


var BoardTopic = createClass({

    getInitialState: function (){
        return {items: this.props.inheritState}
    },

    componentWillReceiveProps: function(nextProps){
	if(nextProps.inheritState){
		this.setState({
			items: nextProps.inheritState
		})
	}
},

    eachHashtag: function (text, i){
        return (<Topic key={i} index={i}>
                    {text}
                </Topic>
           );

    },

    render: function (){
        return (<div className='boardTopic'>
                    {this.state.items.map(this.eachHashtag)}
                </div>)
    }
});


var ChooseTopic = createClass({


    getInitialState: function (){
        return {defaultText: 'Type your hashtag..', items: listaHash,
                hashtags: listaHash}
                },


    filterButtons: function (event){
        var updatedList = this.state.hashtags;
        updatedList = updatedList.filter(function (item){
                                            return item.toLowerCase().search(
                                                    event.target.value.toLowerCase()) !== -1;
                                         });
        this.setState({items: updatedList});
    },


    render: function (){
        return (<div className='TopicContainer'>
                    <h3>Choose</h3>
                    <BoardTopic inheritState={this.state.items.slice(0,5)} />
                </div>)
    }
});

export default ChooseTopic;


//export default BoardTopic;
