create table client_invoices
(
    invoice_id               serial primary key       not null,
    created_date             timestamp with time zone not null,
    due_date                 timestamp with time zone not null,
    payment_date             timestamp with time zone not null,
    amount_to_pay_to_builder decimal                  not null,
    amount_total             decimal                  not null,
    client_id                text                     not null
);

copy client_invoices(
    created_date,
    due_date,
    payment_date,
    amount_to_pay_to_builder,
    amount_total,
    client_id)
        from '/data.csv'
        delimiter ','
        csv header;
