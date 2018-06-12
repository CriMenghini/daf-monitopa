import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import './App.css';
import registerServiceWorker from './registerServiceWorker';
import createClass from 'create-react-class';
import Comment from './Comment';
import BoardHashtag from './Board';
import Hashtag  from './Hashtag';
import SearchBar from './SearchBar';
import App from './App';
import Topic from './Topic';
import 'bootstrap/dist/css/bootstrap.min.css';
import HomePage from './HomePage';



var LandingPage = createClass({

    getInitialState: function (){
        return {choice: false, selection: ''}
    },


    handleChoiceHashtag: function (){
        this.setState({choice: !this.state.choice, selection: 'hash'})
    },

    handleChoiceTopic: function (){
        this.setState({choice: !this.state.choice, selection: 'topic'})
    },




    render: function (){

            if (this.state.choice){

                if (this.state.selection == 'hash')
                        {return (<App {... this.props} {... this.state} scegliAnalisiHash={this.handleChoiceHashtag}/>)}

                else if (this.state.selection == 'topic'){
                        {return (<Topic {... this.props} {... this.state} scegliAnalisiHash={this.handleChoiceTopic}/>)}
                     };


            }
            else {
                return (<HomePage {... this.props} {... this.state} scegliAnalisiHash={this.handleChoiceHashtag} scegliAnalisiTopic={this.handleChoiceTopic}/>)
            };


    }


});



ReactDOM.render(<LandingPage />, document.getElementById('root'));
registerServiceWorker();
