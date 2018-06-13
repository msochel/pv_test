import React, { Component } from 'react';
import {DataTable} from 'primereact/components/datatable/DataTable';
import {Column} from 'primereact/components/column/Column';
import {InputText} from 'primereact/components/inputtext/InputText';
import {Dropdown} from 'primereact/components/dropdown/Dropdown';
import {MultiSelect} from 'primereact/components/multiselect/MultiSelect';
// import './App.css';
// import 'primereact/resources/themes/omega/theme.css';
// import 'primereact/resources/primereact.min.css';
// import 'font-awesome/css/font-awesome.css';

class App extends Component {

    constructor() {
        super();
        this.state = {
            brand: null,
            colors: null,
            cars: [
                {"brand": "VW", "year": 2012, "color": "Orange", "vin": "dsad231ff"},
                {"brand": "Audi", "year": 2011, "color": "Black", "vin": "gwregre345"},
                {"brand": "Renault", "year": 2005, "color": "Gray", "vin": "h354htr"},
                {"brand": "BMW", "year": 2003, "color": "Blue", "vin": "j6w54qgh"},
                {"brand": "Mercedes", "year": 1995, "color": "Orange", "vin": "hrtwy34"},
                {"brand": "Volvo", "year": 2005, "color": "Black", "vin": "jejtyj"},
                {"brand": "Honda", "year": 2012, "color": "Yellow", "vin": "g43gr"},
                {"brand": "Jaguar", "year": 2013, "color": "Orange", "vin": "greg34"},
                {"brand": "Ford", "year": 2000, "color": "Black", "vin": "h54hw5"},
                {"brand": "Fiat", "year": 2013, "color": "Red", "vin": "245t2s"}
            ]
        };
        this.onBrandChange = this.onBrandChange.bind(this);
        this.onColorChange = this.onColorChange.bind(this);
    }

    onBrandChange(event) {
        this.dt.filter(event.value, 'brand', 'equals');
        this.setState({brand: event.value});
    }

    onColorChange(event) {
        this.dt.filter(event.value, 'color', 'in');
        this.setState({colors: event.value});
    }

    render() {
        var header = <div style={{'textAlign':'left'}}>
                        <i className="fa fa-search" style={{margin:'4px 4px 0 0'}}></i>
                        <InputText type="search" onInput={(e) => this.setState({globalFilter: e.target.value})} placeholder="Global Search" size="50"/>
                    </div>;

        let brands = [
                {label: 'All Brands', value: null},
                {label: 'Audi', value: 'Audi'},
                {label: 'BMW', value: 'BMW'},
                {label: 'Fiat', value: 'Fiat'},
                {label: 'Honda', value: 'Honda'},
                {label: 'Jaguar', value: 'Jaguar'},
                {label: 'Mercedes', value: 'Mercedes'},
                {label: 'Renault', value: 'Renault'},
                {label: 'VW', value: 'VW'},
                {label: 'Volvo', value: 'Volvo'}
            ];

        let colors = [
            {label: 'White', value: 'White'},
            {label: 'Green', value: 'Green'},
            {label: 'Silver', value: 'Silver'},
            {label: 'Black', value: 'Black'},
            {label: 'Red', value: 'Red'},
            {label: 'Maroon', value: 'Maroon'},
            {label: 'Brown', value: 'Brown'},
            {label: 'Orange', value: 'Orange'},
            {label: 'Blue', value: 'Blue'}
        ];

        let brandFilter = <Dropdown style={{width: '100%'}} className="ui-column-filter"
                value={this.state.brand} options={brands} onChange={this.onBrandChange}/>

        let colorFilter = <MultiSelect style={{width:'100%'}} className="ui-column-filter"
            value={this.state.colors} options={colors} onChange={this.onColorChange}/>

        return (
          <div>
              <h1>Table Section </h1>
              <div className="content-section implementation">
                  <DataTable ref={(el) => this.dt = el} value={this.state.cars} paginator={true} rows={10} header={header}
                      globalFilter={this.state.globalFilter}>
                      <Column field="vin" header="Vin" filter={true} filterMatchMode="contains"/>
                      <Column field="year" header="Year" filter={true} filterMatchMode="contains"/>
                      <Column field="brand" header="Brand" filter={true} filterElement={brandFilter} />
                      <Column field="color" header="Color" filter={true} filterElement={colorFilter} />
                  </DataTable>
              </div>
          </div>
        );
    }
}

export default App;
