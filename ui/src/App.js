import React, { Component } from 'react';
import {DataTable} from 'primereact/components/datatable/DataTable';
import {Column} from 'primereact/components/column/Column';
import {InputText} from 'primereact/components/inputtext/InputText';
import {MultiSelect} from 'primereact/components/multiselect/MultiSelect';
import {Dropdown} from 'primereact/components/dropdown/Dropdown';
import request from 'superagent';


class App extends Component {

    constructor() {
        super();
        this.state = {
            source : null,
            status: null,
            interactions: [ ],
        };
        this.ComponentDidMount();
        this.onStatusChange = this.onStatusChange.bind(this);
        this.onSourceChange = this.onSourceChange.bind(this);
    }

    ComponentDidMount() {
      request
      .get('http://localhost/backend/get_ticket')
      .set('Accept', 'application/json')
      .then(res => {
        this.setState({
          interactions: res.body.data
        });
        console.log(res)
      })
      .catch(err => {
        console.log(err);
      });
    }

    onStatusChange(event) {
        this.dt.filter(event.value, 'status', 'equals');
        this.setState({status: event.value});
    }

    onSourceChange(event) {
    this.dt.filter(event.value, 'source', 'in');
    this.setState({source: event.value});
    }

    render() {
      var header = <div style={{'textAlign':'left'}}>
                      <i className="fa fa-search" style={{margin:'4px 4px 0 0'}}></i>
                      <InputText type="search" onInput={(e) => this.setState({globalFilter: e.target.value})} placeholder="Global Search" size="50"/>
                  </div>;

          let source = [
              {label: 'Email', value: 'Email'},
              {label: 'Portal', value: 'Portal'},
              {label: 'Phone', value: 'Phone'},
              {label: 'Chat', value: 'Chat'},
              {label: 'Mobihelp', value: 'Mobihelp'},
              {label: 'Feedback Widget', value: 'Feedback Widget'},
              {label: 'Outbound Email', value: 'Outbound Email'},
          ];

          let status = [
              {label: 'All status', value: null},
              {label: 'Open', value: 'Open'},
              {label: 'Pending', value: 'Pending'},
              {label: 'Resolved', value: 'Resolved'},
              {label: 'Closed', value: 'Closed'},
          ];

        let sourceFilter = <MultiSelect style={{width:'100%'}} className="ui-column-filter"
            value={this.state.source} options={source} onChange={this.onSourceChange}/>

        let statusFilter = <Dropdown style={{width: '100%'}} className="ui-column-filter"
            value={this.state.status} options={status} onChange={this.onStatusChange}/>

        return (
          <div>
              <h1>Table  </h1>
              <div className="content-section implementation">
                <DataTable ref={(el) => this.dt = el} value={this.state.interactions} paginator={true} responsive={true} rows={10} header={header}
                      globalFilter={this.state.globalFilter}>
                      <Column field="name" header="Name" filter={true} filterMatchMode="contains" sortable={true} />
                      <Column field="description" header="Description" filter={true} filterMatchMode="contains"/>
                      <Column field="priority" header="Priority" filter={true} filterMatchMode="contains"/>
                      <Column field="source" header="Source" filter={true} filterElement={sourceFilter}/>
                      <Column field="status" header="Status" filter={true} filterElement={statusFilter}/>
                      <Column field="type" header="Type" filter={true} filterMatchMode="contains"/>
                      <Column field="updated_at" header="Date" filter={true}  sortable={true} />
                  </DataTable>
              </div>
          </div>
        );
    }
}

export default App;
