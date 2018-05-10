import React, { Component } from 'react';
import createClass from 'create-react-class';
import './Hashtag.css';
import BoardHashtag from './Board';


var Hashtag = createClass({

        render: function (){
            return (<div className='Hashtag'>
                        <form action="/hello" method="post">
                            <button className='tag' name='selectedHashtag' value={this.props.children}>#{this.props.children}</button>
                        </form>
                    </div>);
        }
});




export default Hashtag;
