import React, { Component } from 'react';
import createClass from 'create-react-class';
import App from './App.css';
import BoardHashtag from './Board';
import Hashtag  from './Hashtag';
import name_topic from './data/name_topic.js';
import Particles from 'react-particles-js';


var SearchBarTopic = createClass({


    getInitialState: function (){
        return {defaultText: 'Type your hashtag..', items: name_topic,
                hashtags: name_topic}
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
        return (<div className='SearchContainer'>
                    <h3 className='search-title my-3'>Scegli il topic!</h3>

                    <form>
                        <input className='input-mine my-3' type="text" placeholder={this.state.defaultText} onChange={this.filterButtons} name='hashtag' />
                    </form>

                    <Particles
                        params={{particles: {number: {value: 30},
                                             color: {value: '#cf2c2c'},
                                             },

                                             }}
                                      style={{
                                        position: 'absolute',
                                        zIndex: 0,
                                        height: '100%',
                                        width: '100%'
                                      }}/>

                    <BoardHashtag inheritState={this.state.items.slice(0,60)}  { ...this.props } { ...this.state} funzioneSubmit={this.props.funzioneSubmit} funzioneClick={this.props.funzioneClick}/>
                </div>)
    }
});

export default SearchBarTopic;

// Get reference to one of my child: to call ref: variable = this.refs.newHash.value
// when buttons belong to other components: how do we call functions? Properties: you can pass entire function
// to <Hashtag updateText={this.updateComment}>  to recall the function in another function: this.props.NAME_FUNCTION
// the same stands for other properties.