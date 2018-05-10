import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import createClass from 'create-react-class';
import Comment from './Comment';
import BoardHashtag from './Board';
import Hashtag  from './Hashtag';
import SearchBar from './SearchBar';



var CheckBox = createClass({

    getInitialState: function (){
        return {checked: true}
    },


    handleChecked: function (){
        this.setState({checked: !this.state.checked})
    },


    render: function (){

            var msg;
            if (this.state.checked){
                msg = 'checked'
            }
            else {msg = 'unchecked'}

        return (
            <div>
                <input type='checkbox' onChange={this.handleChecked} defaultChecked={this.state.checked}/>
                <h3>Checkbox is {msg}</h3>
            </div>
        );

    }


});



ReactDOM.render(<div>
                    <SearchBar />
                </div>, document.getElementById('root'));
registerServiceWorker();
