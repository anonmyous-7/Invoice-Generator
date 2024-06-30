import datetime

class InvoiceGenerator:
    def __init__(self, company_name, company_address, company_phone):
        self.company_name = company_name
        self.company_address = company_address
        self.company_phone = company_phone
        self.items = []
        self.total_amount = 0

    def add_item(self, description, quantity, price):
        self.items.append({"description": description, "quantity": quantity, "price": price})
        self.total_amount += quantity * price

    def generate_invoice(self, client_name, client_address, invoice_number):
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; }}
                .invoice-box {{ max-width: 800px; margin: auto; padding: 30px; border: 1px solid #eee; box-shadow: 0 0 10px rgba(0, 0, 0, 0.15); }}
                .invoice-box table {{ width: 100%; line-height: inherit; text-align: left; }}
                .invoice-box table td {{ padding: 5px; vertical-align: top; }}
                .invoice-box table tr td:nth-child(2) {{ text-align: right; }}
                .invoice-box table tr.top table td {{ padding-bottom: 20px; }}
                .invoice-box table tr.top table td.title {{ font-size: 45px; line-height: 45px; color: #333; }}
                .invoice-box table tr.information table td {{ padding-bottom: 40px; }}
                .invoice-box table tr.heading td {{ background: #eee; border-bottom: 1px solid #ddd; font-weight: bold; }}
                .invoice-box table tr.item td {{ border-bottom: 1px solid #eee; }}
                .invoice-box table tr.item.last td {{ border-bottom: none; }}
                .invoice-box table tr.total td:nth-child(2) {{ border-top: 2px solid #eee; font-weight: bold; }}
            </style>
        </head>
        <body>
            <div class="invoice-box">
                <table cellpadding="0" cellspacing="0">
                    <tr class="top">
                        <td colspan="2">
                            <table>
                                <tr>
                                    <td class="title">
                                        {self.company_name}
                                    </td>
                                    <td>
                                        Invoice #: {invoice_number}<br>
                                        Created: {current_date}
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr class="information">
                        <td colspan="2">
                            <table>
                                <tr>
                                    <td>
                                        {self.company_name}<br>
                                        {self.company_address}<br>
                                        {self.company_phone}
                                    </td>
                                    <td>
                                        {client_name}<br>
                                        {client_address}
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr class="heading">
                        <td>
                            Item
                        </td>
                        <td>
                            Price
                        </td>
                    </tr>
        """

        for item in self.items:
            item_total = item["quantity"] * item["price"]
            html_content += f"""
            <tr class="item">
                <td>
                    {item["description"]} (x{item["quantity"]})
                </td>
                <td>
                    ${item_total:.2f}
                </td>
            </tr>
            """

        html_content += f"""
                    <tr class="total">
                        <td></td>
                        <td>
                            Total: ${self.total_amount:.2f}
                        </td>
                    </tr>
                </table>
            </div>
        </body>
        </html>
        """

        invoice_file = f"Invoice_{invoice_number}.html"
        with open(invoice_file, 'w') as file:
            file.write(html_content)
        print(f"Invoice generated: {invoice_file}")

# Example usage
invoice = InvoiceGenerator("My Company", "1234 Street Address, City, Country", "123-456-7890")
invoice.add_item("Product 1", 2, 150)
invoice.add_item("Product 2", 1, 299.99)
invoice.add_item("Service 1", 5, 75)

invoice.generate_invoice("Client Name", "5678 Client Address, City, Country", "0001")
