
The API will be available at http://localhost:8000/.

## Usage

### Projects

- `GET /projects/`: Retrieve a list of all projects.
- `POST /projects/`: Create a new project.
- `GET /projects/<project_id>/`: Retrieve details of a specific project.
- `PUT /projects/<project_id>/`: Update details of a specific project.
- `DELETE /projects/<project_id>/`: Delete a project.

### Deals

- `GET /deals/`: Retrieve a list of all deals.
- `POST /deals/`: Create a new deal.
- `GET /deals/<deal_id>/`: Retrieve details of a specific deal.
- `PUT /deals/<deal_id>/`: Update details of a specific deal.
- `DELETE /deals/<deal_id>/`: Delete a deal.
- `GET /deals/<deal_id>/tax-credit-amount/`: Get the total tax credit transfer amount for a deal.

## Data Modeling

- Each Project represents a clean energy project and includes fields for name, fair market value (FMV), and transfer rate.
- Each Deal represents a financial transaction and includes a unique name and a Many-to-Many relationship with projects.
- The tax credit transfer amount for a project in a deal is calculated as FMV * 0.3 * transfer_rate.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

# backend-assignment
