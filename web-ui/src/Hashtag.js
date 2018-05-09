import React, { Component } from 'react';
import createClass from 'create-react-class';
import './Hashtag.css';
import BoardHashtag from './Board';


var Hashtag = createClass({



        render: function (){
            return (<div className='Hashtag'>


                        <button className='tag'>#{this.props.children}</button>

                    </div>);
        }
});




export default Hashtag;
