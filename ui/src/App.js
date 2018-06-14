import React, { Component } from 'react';
import {DataTable} from 'primereact/components/datatable/DataTable';
import {Column} from 'primereact/components/column/Column';
import {InputText} from 'primereact/components/inputtext/InputText';
import request from 'superagent';


class App extends Component {

    constructor() {
        super();
        this.state = {
            interactions: [ ]
        };
        this.ComponentDidMount();
    }

    ComponentDidMount() {
      request
      .get('http://localhost/backend/get')
      .set('Accept', 'application/json')
      .then(res => {
        this.setState({
          interactions: res.body.data
        });
        console.log("Me montaron")
      })
      .catch(err => {
        console.log(err);
      });
    }

    render() {
      var header = <div style={{'textAlign':'left'}}>
                      <i className="fa fa-search" style={{margin:'4px 4px 0 0'}}></i>
                      <InputText type="search" onInput={(e) => this.setState({globalFilter: e.target.value})} placeholder="Global Search" size="50"/>
                  </div>;
        return (
          <div>
              <h1>Table  </h1>
              <div className="content-section implementation">
                <DataTable ref={(el) => this.dt = el} value={this.state.interactions} paginator={true} rows={10} header={header}
                      globalFilter={this.state.globalFilter}>
                      <Column field="name" header="Name" filter={true} filterMatchMode="contains"/>
                      <Column field="description" header="Description" filter={true} filterMatchMode="contains"/>
                      <Column field="priority" header="Priority" filter={true} sortable={true} />
                      <Column field="source" header="Source" filter={true} />
                      <Column field="status" header="Status" filter={true} />
                      <Column field="type" header="Type" filter={true} />
                      <Column field="updated_at" header="Date" filter={true}  sortable={true}/>
                  </DataTable>
              </div>
          </div>
        );
    }
}

export default App;
