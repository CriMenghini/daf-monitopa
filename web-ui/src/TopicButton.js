import React, { Component } from 'react';
import createClass from 'create-react-class';
import './App.css';
import listaHash from './data/listaHash.js';


var Topic = createClass({

        render: function (){
            return (<div className='Topic'>
                        <form onSubmit={this.props.funzioneSubmit}>
                            <button className='tag' name='selectedHashtag' value={this.props.children} onClick={this.props.funzioneClick}>#{this.props.children}</button>
                        </form>
                    </div>);
        }
});


export default Topic;

