# JAQueL: An intuitive query language for measurement data based on ASAM ODS

JAQueL stands for "**J**son **A**SAM ODS **Qu**ery **L**anguage" and is
a lightweight wrapper on the standardized [ASAM ODS REST
API](https://www.asam.net/standards/detail/ods/wiki/).

JAQueL allows you to query your data in a simple and intuitive way
following the concepts of the [MongoDB Query Language
(MQL)](https://www.mongodb.com). The definition of query expression as
JSON easily integrates with the Python language - a win-win situation
when exploring data programmatically.

## Short introduction to JAQueL

As mentioned above, JAQueL is derived from MQL, but it’s not the same.
The objects or entities (application elements) of ASAM ODS can be
compared to 'collections' in MQL. However, JAQueL treats 'collections'
in the same way as 'documents', meaning entities are part of the query
expression.

Lets start with some simple query examples to familiarize you with the
concept:

### Simple query examples

#### Select all instances of a certain entity

Lets assume, you want to see all "Units" defined in the unit catalog of
your Peak ODS Server:

##### JAQueL

    {
        "Unit": {}
    }

##### ods.SelectStatement

    {
      "columns": [
        {
          "aid": "54",
          "attribute": "*"
        }
      ]
    }

For those of you, who are not familiar with ASAM ODS queries, the
corresponding SQL statement would look like this:

    SELECT * FROM Unit

This is the "one SQL example", in the course of this documentation. We
will focus on JAQueL and its corresponding ASAM ODS queries (to let you
compare your options).

#### Queries for any data model

ASAM ODS has the concept of a base model (you can think of as semantic
templates), which you can use to create your own data model - the
application model. To define queries, which work on any data model, you
can use the names of the base model instead of the application model
name.

For "Unit" the base name is "AoUnit", so the generic query would be:

##### JAQueL (base entity name)

    {
        "AoUnit": {}
    }

##### ods.SelectStatement (-)

    {
      "columns": [
        {
          "aid": "54",
          "attribute": "*"
        }
      ]
    }

For "AoUnit" the generic approach delivers the expected result. But be
careful with those base entities, which are used to define several
different application entities, for example AoSubtest,
AoTestSequencePart,…​ In this case, JAQueL will return results for the
first found derived application entities.

You can also use the base names when dealing with `attributes`. This is
very handy, in case you don’t want to look-up application names.

#### Query for instances of a certain ID

A very typical use-case is searching for a specific instance of a known
ID (for instance in case something has been selected by a user or
process). To do so you place the condition inside the curly brackets (in
our example the id in question is 42).

##### JAQueL (by id)

    {
        "AoUnit": {
            "id": 42
        }
    }

##### ods.SelectStatement (by id)

    {
      "columns": [
        {
          "aid": "54",
          "attribute": "*"
        }
      ],
      "where": [
        {
          "condition": {
            "aid": "54",
            "attribute": "Id",
            "longlongArray": {
              "values": [
                "42"
              ]
            }
          }
        }
      ]
    }

#### Query for instances with a certain name

As popular as searching for an id is searching for instances of a
certain name. In case you only specify the name, the default query
operator is `$eq`. In the example below we’re searching for the
engineering unit "s" (second).

##### JAQueL (by name)

    {
        "AoUnit": {
            "name": "s"
        }
    }

##### ods.SelectStatement (by name)

    {
      "columns": [
        {
          "aid": "54",
          "attribute": "*"
        }
      ],
      "where": [
        {
          "condition": {
            "aid": "54",
            "attribute": "Name",
            "stringArray": {
              "values": [
                "s"
              ]
            }
          }
        }
      ]
    }

In case you don’t know if there exists also "seconds with a capital S"
(you remember Power of Tower), you can try a case insensitive query - in
the example below also the equal-operator `$eq` is now defined.

##### JAQueL (case insensitive)

    {
        "AoUnit": {
            "name": {
                "$eq": "s"
            },
            "$options": "i"
        }
    }

##### ods.SelectStatement (case insensitive)

    {
      "columns": [
        {
          "aid": "54",
          "attribute": "*"
        }
      ],
      "where": [
        {
          "condition": {
            "aid": "54",
            "attribute": "Name",
            "operator": "OP_CI_EQ",
            "stringArray": {
              "values": [
                "s"
              ]
            }
          }
        }
      ]
    }

In case you’re looking for units starting with a certain character you
have to use the `$like`-operator instead. You can also combine the
`$like`-operator with the case-insensitive option:

##### JAQueL ($like)

    {
        "AoUnit": {
            "name": {
                "$like": "k*"
            },
            "$options": "i"
        }
    }

##### ods.SelectStatement (OP_CI_LIKE)

    {
      "columns": [
        {
          "aid": "54",
          "attribute": "*"
        }
      ],
      "where": [
        {
          "condition": {
            "aid": "54",
            "attribute": "Name",
            "operator": "OP_CI_LIKE",
            "stringArray": {
              "values": [
                "k*"
              ]
            }
          }
        }
      ]
    }

### Other query operators

In this section, we show you how to use other query operators (see
[Condition Operators](#condition-operators)) like between, less and greater.
And you’ll also see, how to deal with time values. Lets start with
between and get measurements that started in a certain time interval:

#### JAQueL ($between)

    {
        "AoMeasurement": {
            "measurement_begin": {
                "$between": [
                    "20001223000000",
                    "20241224000000"
                ]
            }
        },
        "$options": {
            "$rowlimit": 5
        }
    }

#### ods.SelectStatement (OP_BETWEEN)

    {
      "columns": [
        {
          "aid": "79",
          "attribute": "*"
        }
      ],
      "where": [
        {
          "condition": {
            "aid": "79",
            "attribute": "MeasurementBegin",
            "operator": "OP_BETWEEN",
            "stringArray": {
              "values": [
                "20001223000000",
                "20241224000000"
              ]
            }
          }
        }
      ],
      "rowLimit": "5"
    }

The upper example is using the ASAM ODS date-time format, with JAQueL
you can also use the ISO time (ISO 8601) instead:

#### JAQueL (ISO time - ISO 8601)

    {
        "AoMeasurement": {
            "measurement_begin": {
                "$between": [
                    "2000-04-22T00:00:00.001Z",
                    "2024-04-23T00:00:00.002Z"
                ]
            }
        },
        "$options": {
            "$rowlimit": 5
        }
    }

#### ods.SelectStatement (ASAM TIME)

    {
      "columns": [
        {
          "aid": "79",
          "attribute": "*"
        }
      ],
      "where": [
        {
          "condition": {
            "aid": "79",
            "attribute": "MeasurementBegin",
            "operator": "OP_BETWEEN",
            "stringArray": {
              "values": [
                "20000422000000001",
                "20240423000000002"
              ]
            }
          }
        }
      ],
      "rowLimit": "5"
    }

You can, for instance, also search for channels in a specific data range
like using "greater than" (`$gt`, `$gte`) respective "smaller than"
(`$lt`, `$lte`):

#### JAQueL (`$gt`, `$lt`)

    {
        "AoMeasurementQuantity": {
            "maximum": {
                "$gt": 0.0,
                "$lt": 12000.0
            }
        },
        "$options": {
            "$rowlimit": 5
        }
    }

#### ods.SelectStatement (OP_GT, OP_LT)

    {
      "columns": [
        {
          "aid": "80",
          "attribute": "*"
        }
      ],
      "where": [
        {
          "condition": {
            "aid": "80",
            "attribute": "Maximum",
            "operator": "OP_GT",
            "doubleArray": {
              "values": [
                0.0
              ]
            }
          }
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "condition": {
            "aid": "80",
            "attribute": "Maximum",
            "operator": "OP_LT",
            "doubleArray": {
              "values": [
                12000.0
              ]
            }
          }
        }
      ],
      "rowLimit": "5"
    }

You can configure Peak ODS Server to automatically calculate the
minimum, maximum, average and standard deviation values for your
measurement data!

### Define the return data

In the above examples always all attributes of the entity in question
has been returned. In this section we show you how to reduce or further
define the attributes to be returned.

#### Specify the return attributes

In case you’re not interested in getting returned all of the attributes
of the entity in question, you can reduce them to the ones you need:
Lets reduce the attributes in return to three, by defining
`$attributes` - in our unit example "name", "factor" and "offset":

##### JAQueL (`$attributes`)

    {
        "Unit": {},
        "$attributes": {
            "name": 1,
            "factor": 1,
            "offset": 1
        }
    }

##### ods.SelectStatement (columns)

    {
      "columns": [
        {
          "aid": "54",
          "attribute": "Name"
        },
        {
          "aid": "54",
          "attribute": "Factor"
        },
        {
          "aid": "54",
          "attribute": "Offset"
        }
      ]
    }

Ok. That was easy. But what if you’re interested in return values not
directly available at the entity in question but at a referenced entity?

In the ASAM data model engineering units always have a "physical
dimension" relation which defines the SI-unit exponents for that unit
(and are the basis for unit conversion with related units). How to get
those "physical dimension" in return? The answer is: Simply add those to
the `$attributes` (result) definition:

##### JAQueL (-)

    {
        "Unit": {},
        "$attributes": {
            "name": 1,
            "factor": 1,
            "offset": 1,
            "phys_dimension.name": 1,
            "phys_dimension.length_exp": 1,
            "phys_dimension.mass_exp": 1
        }
    }

##### ods.SelectStatement (joins)

    {
      "columns": [
        {
          "aid": "54",
          "attribute": "Name"
        },
        {
          "aid": "54",
          "attribute": "Factor"
        },
        {
          "aid": "54",
          "attribute": "Offset"
        },
        {
          "aid": "47",
          "attribute": "Name"
        },
        {
          "aid": "47",
          "attribute": "Length"
        },
        {
          "aid": "47",
          "attribute": "Mass"
        }
      ],
      "joins": [
        {
          "aidFrom": "54",
          "aidTo": "47",
          "relation": "PhysDimension"
        }
      ]
    }

You can also do this in a more compact way:

##### JAQueL (--)

    {
        "Unit": {},
        "$attributes": {
            "name": 1,
            "factor": 1,
            "offset": 1,
            "phys_dimension": {
                "name": 1,
                "length_exp": 1,
                "mass_exp": 1
            }
        }
    }

##### ods.SelectStatement (--)

    {
      "columns": [
        {
          "aid": "54",
          "attribute": "Name"
        },
        {
          "aid": "54",
          "attribute": "Factor"
        },
        {
          "aid": "54",
          "attribute": "Offset"
        },
        {
          "aid": "47",
          "attribute": "Name"
        },
        {
          "aid": "47",
          "attribute": "Length"
        },
        {
          "aid": "47",
          "attribute": "Mass"
        }
      ],
      "joins": [
        {
          "aidFrom": "54",
          "aidTo": "47",
          "relation": "PhysDimension"
        }
      ]
    }

Or you can retrieve all attributes (of a related entity) using the
asterix "\*":

##### JAQueL (*)

    {
        "Unit": {},
        "$attributes": {
            "name": 1,
            "factor": 1,
            "offset": 1,
            "phys_dimension.*": 1
        }
    }

##### ods.SelectStatement (*)

    {
      "columns": [
        {
          "aid": "54",
          "attribute": "Name"
        },
        {
          "aid": "54",
          "attribute": "Factor"
        },
        {
          "aid": "54",
          "attribute": "Offset"
        },
        {
          "aid": "47",
          "attribute": "*"
        }
      ],
      "joins": [
        {
          "aidFrom": "54",
          "aidTo": "47",
          "relation": "PhysDimension"
        }
      ]
    }

#### Limit the amounts of results

In addition to specifying which attributes (columns) to be returned you
can also limit the number of rows by defining a `$rowlimit`:

##### JAQueL ($rowlimit)

    {
        "AoUnit": {},
        "$options": {
            "$rowlimit": 5
        }
    }

##### ods.SelectStatement (rowLimit)

    {
      "columns": [
        {
          "aid": "54",
          "attribute": "*"
        }
      ],
      "rowLimit": "5"
    }

#### Order results by 'name'

You can order your result set by defining an "orderby" statement - in
our case we order the result by "name".

##### JAQueL ($orderby)

    {
        "AoUnit": {},
        "$attributes": {
            "id": 1,
            "name": 1
        },
        "$orderby": {
            "name": 1
        }
    }

##### ods.SelectStatement (orderBy)

    {
      "columns": [
        {
          "aid": "54",
          "attribute": "Id"
        },
        {
          "aid": "54",
          "attribute": "Name"
        }
      ],
      "orderBy": [
        {
          "aid": "54",
          "attribute": "Name"
        }
      ]
    }

### Use entity relations in query expressions

In the above examples you’ve seen how to specify certain attributes in
the result set - even attributes of related entities. You can also use
those relations in query expressions.

In the example below, we’re searching for units defining 'speed', so the
SI-unit exponents for length must be 1, whereas the one for time has to
be -1 - like in m/s. All other SI-unit exponents must be 0 in that case.

#### JAQueL ()

    {
        "AoUnit": {
            "phys_dimension": {
                "length_exp": 1,
                "mass_exp": 0,
                "time_exp": -1,
                "current_exp": 0,
                "temperature_exp": 0,
                "molar_amount_exp": 0,
                "luminous_intensity_exp": 0
            }
        },
        "$attributes": {
            "name": 1,
            "factor": 1,
            "offset": 1,
            "phys_dimension.name": 1
        }
    }

#### ods.SelectStatement (joins  )

    {
      "columns": [
        {
          "aid": "54",
          "attribute": "Name"
        },
        {
          "aid": "54",
          "attribute": "Factor"
        },
        {
          "aid": "54",
          "attribute": "Offset"
        },
        {
          "aid": "47",
          "attribute": "Name"
        }
      ],
      "where": [
        {
          "condition": {
            "aid": "47",
            "attribute": "Length",
            "longArray": {
              "values": [
                1
              ]
            }
          }
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "Mass",
            "longArray": {
              "values": [
                0
              ]
            }
          }
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "Time",
            "longArray": {
              "values": [
                -1
              ]
            }
          }
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "Current",
            "longArray": {
              "values": [
                0
              ]
            }
          }
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "Temperature",
            "longArray": {
              "values": [
                0
              ]
            }
          }
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "MolarAmount",
            "longArray": {
              "values": [
                0
              ]
            }
          }
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "LuminousIntensity",
            "longArray": {
              "values": [
                0
              ]
            }
          }
        }
      ],
      "joins": [
        {
          "aidFrom": "54",
          "aidTo": "47",
          "relation": "PhysDimension"
        }
      ]
    }

BTW: This way you get in return all 'speed' units which you can use for
unit conversion of your speed measurement results (for instance from
km/h to mph) - the Peak ODS Server can do this for you 😉.

### Use conjunctions (and/or)

In this section you learn how to use conjunctions ('AND' respective
'OR' - see [Condition Conjunctions](#condition-conjunctions) in query
expression. In the above example we found units defining 'speed', by
defining all SI-unit exponents in the needed way. You may have
recognized that this means all SI-unit exponents has been combined using
an implicit `$and` conjunction. Below is the exact same search but with
explicit `$and` conjunction:

#### JAQueL ($and)

    {
        "AoUnit": {
            "phys_dimension": {
                "$and": [
                    {
                        "length_exp": 1
                    },
                    {
                        "mass_exp": 0
                    },
                    {
                        "time_exp": -1
                    },
                    {
                        "current_exp": 0
                    },
                    {
                        "temperature_exp": 0
                    },
                    {
                        "molar_amount_exp": 0
                    },
                    {
                        "luminous_intensity_exp": 0
                    }
                ]
            }
        },
        "$attributes": {
            "name": 1,
            "factor": 1,
            "offset": 1,
            "phys_dimension.name": 1
        }
    }

#### ods.SelectStatement (CO_AND)

    {
      "columns": [
        {
          "aid": "54",
          "attribute": "Name"
        },
        {
          "aid": "54",
          "attribute": "Factor"
        },
        {
          "aid": "54",
          "attribute": "Offset"
        },
        {
          "aid": "47",
          "attribute": "Name"
        }
      ],
      "where": [
        {
          "conjunction": "CO_OPEN"
        },
        {
          "conjunction": "CO_OPEN"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "Length",
            "longArray": {
              "values": [
                1
              ]
            }
          }
        },
        {
          "conjunction": "CO_CLOSE"
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "conjunction": "CO_OPEN"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "Mass",
            "longArray": {
              "values": [
                0
              ]
            }
          }
        },
        {
          "conjunction": "CO_CLOSE"
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "conjunction": "CO_OPEN"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "Time",
            "longArray": {
              "values": [
                -1
              ]
            }
          }
        },
        {
          "conjunction": "CO_CLOSE"
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "conjunction": "CO_OPEN"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "Current",
            "longArray": {
              "values": [
                0
              ]
            }
          }
        },
        {
          "conjunction": "CO_CLOSE"
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "conjunction": "CO_OPEN"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "Temperature",
            "longArray": {
              "values": [
                0
              ]
            }
          }
        },
        {
          "conjunction": "CO_CLOSE"
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "conjunction": "CO_OPEN"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "MolarAmount",
            "longArray": {
              "values": [
                0
              ]
            }
          }
        },
        {
          "conjunction": "CO_CLOSE"
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "conjunction": "CO_OPEN"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "LuminousIntensity",
            "longArray": {
              "values": [
                0
              ]
            }
          }
        },
        {
          "conjunction": "CO_CLOSE"
        },
        {
          "conjunction": "CO_CLOSE"
        }
      ],
      "joins": [
        {
          "aidFrom": "54",
          "aidTo": "47",
          "relation": "PhysDimension"
        }
      ]
    }

Now assume, we’re interest in units defining speed and time (logical
speed `$or` time ) - below you see the resulting query. BTW, the
corresponding ods.SelectStatement is very expressive or impressive …​

##### JAQueL ($or)

    {
        "AoUnit": {
            "phys_dimension": {
                "$or": [
                    {
                        "length_exp": 1,
                        "mass_exp": 0,
                        "time_exp": -1,
                        "current_exp": 0,
                        "temperature_exp": 0,
                        "molar_amount_exp": 0,
                        "luminous_intensity_exp": 0
                    },
                    {
                        "length_exp": 0,
                        "mass_exp": 0,
                        "time_exp": 1,
                        "current_exp": 0,
                        "temperature_exp": 0,
                        "molar_amount_exp": 0,
                        "luminous_intensity_exp": 0
                    }
                ]
            }
        },
        "$attributes": {
            "name": 1,
            "factor": 1,
            "offset": 1,
            "phys_dimension.name": 1
        }
    }

##### ods.SelectStatement (CO_OR)

    {
      "columns": [
        {
          "aid": "54",
          "attribute": "Name"
        },
        {
          "aid": "54",
          "attribute": "Factor"
        },
        {
          "aid": "54",
          "attribute": "Offset"
        },
        {
          "aid": "47",
          "attribute": "Name"
        }
      ],
      "where": [
        {
          "conjunction": "CO_OPEN"
        },
        {
          "conjunction": "CO_OPEN"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "Length",
            "longArray": {
              "values": [
                1
              ]
            }
          }
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "Mass",
            "longArray": {
              "values": [
                0
              ]
            }
          }
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "Time",
            "longArray": {
              "values": [
                -1
              ]
            }
          }
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "Current",
            "longArray": {
              "values": [
                0
              ]
            }
          }
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "Temperature",
            "longArray": {
              "values": [
                0
              ]
            }
          }
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "MolarAmount",
            "longArray": {
              "values": [
                0
              ]
            }
          }
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "LuminousIntensity",
            "longArray": {
              "values": [
                0
              ]
            }
          }
        },
        {
          "conjunction": "CO_CLOSE"
        },
        {
          "conjunction": "CO_OR"
        },
        {
          "conjunction": "CO_OPEN"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "Length",
            "longArray": {
              "values": [
                0
              ]
            }
          }
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "Mass",
            "longArray": {
              "values": [
                0
              ]
            }
          }
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "Time",
            "longArray": {
              "values": [
                1
              ]
            }
          }
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "Current",
            "longArray": {
              "values": [
                0
              ]
            }
          }
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "Temperature",
            "longArray": {
              "values": [
                0
              ]
            }
          }
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "MolarAmount",
            "longArray": {
              "values": [
                0
              ]
            }
          }
        },
        {
          "conjunction": "CO_AND"
        },
        {
          "condition": {
            "aid": "47",
            "attribute": "LuminousIntensity",
            "longArray": {
              "values": [
                0
              ]
            }
          }
        },
        {
          "conjunction": "CO_CLOSE"
        },
        {
          "conjunction": "CO_CLOSE"
        }
      ],
      "joins": [
        {
          "aidFrom": "54",
          "aidTo": "47",
          "relation": "PhysDimension"
        }
      ]
    }

### Advanced query expression

#### Aggregates

JAQueL provides several aggregate functions such as `$min`, `$max`,
`$dcount`, `$distinct` and other (see [Condition Aggregates](#condition-aggregates)). In this first example you see how
the `$dcount` works counting unique(distinct) unit descriptions:

##### JAQueL ($dcount)

    {
        "AoUnit": {},
        "$attributes": {
            "description": {
                "$dcount": 1
            }
        }
    }

##### ods.SelectStatement (AG_DCOUNT)

    {
      "columns": [
        {
          "aid": "54",
          "attribute": "Description",
          "aggregate": "AG_DCOUNT"
        }
      ]
    }

You can also get the \`$distinct values of unit description:

##### JAQueL ($distinct)

    {
        "AoUnit": {},
        "$attributes": {
            "description": {
                "$distinct": 1
            }
        }
    }

##### ods.SelectStatement (AG_DISTINCT)

    {
      "columns": [
        {
          "aid": "54",
          "attribute": "Description",
          "aggregate": "AG_DISTINCT"
        }
      ]
    }

Or the minimum and maximum of the unit’s scaling factor and offset:

##### JAQueL ($min, $max)

    {
        "AoUnit": {},
        "$attributes": {
            "factor": {
                "$max": 1,
                "$min": 1
            },
            "offset": {
                "$max": 1,
                "$min": 1
            }
        }
    }

##### ods.SelectStatement (AG_MIN, AG_MAX)

    {
      "columns": [
        {
          "aid": "54",
          "attribute": "Factor",
          "aggregate": "AG_MAX"
        },
        {
          "aid": "54",
          "attribute": "Factor",
          "aggregate": "AG_MIN"
        },
        {
          "aid": "54",
          "attribute": "Offset",
          "aggregate": "AG_MAX"
        },
        {
          "aid": "54",
          "attribute": "Offset",
          "aggregate": "AG_MIN"
        }
      ]
    }

#### Group by

Another important query building block is grouping using the '$groupby'
clause. We’re switching to a different entity (AoMeasurement - the
measurement level) in the data model, as there’s typically more to group
and see 😉. And here we group the query results by "name" and
"description".

##### JAQueL ($groupby)

    {
        "AoMeasurement": {},
        "$attributes": {
            "name": 1,
            "description": 1
        },
        "$orderby": {
            "name": 1
        },
        "$groupby": {
            "name": 1,
            "description": 1
        }
    }

##### ods.SelectStatement (groupBy)

    {
      "columns": [
        {
          "aid": "79",
          "attribute": "Name"
        },
        {
          "aid": "79",
          "attribute": "Description"
        }
      ],
      "orderBy": [
        {
          "aid": "79",
          "attribute": "Name"
        }
      ],
      "groupBy": [
        {
          "aid": "79",
          "attribute": "Name"
        },
        {
          "aid": "79",
          "attribute": "Description"
        }
      ]
    }

Typically you may want to combine grouping and counting (aggregates), so
here’s an example for you (on the measurement’s channel level:
AoMeasurementquantity):

##### JAQueL ($count)

    {
        "AoMeasurementquantity": {},
        "$attributes": {
            "name": 1,
            "description": {
               "$count": 1
            }
        },
        "$orderby": {
            "name": 1
        },
        "$groupby": {
            "name": 1,
            "description": 1
        }
    }

##### ods.SelectStatement (AG_COUNT)

    {
      "columns": [
        {
          "aid": "80",
          "attribute": "Name"
        },
        {
          "aid": "80",
          "attribute": "Description",
          "aggregate": "AG_COUNT"
        }
      ],
      "orderBy": [
        {
          "aid": "80",
          "attribute": "Name"
        }
      ],
      "groupBy": [
        {
          "aid": "80",
          "attribute": "Name"
        },
        {
          "aid": "80",
          "attribute": "Description"
        }
      ]
    }

#### Joins

When using entity relations in results it is helpful to decide whether
to use an INNER or OUTER JOIN when getting the results back. We’ve used
INNER JOINS before in "[Use entity relations in query expressions](#use-entity-relations-in-query-expressions)" as they are the default when using entity relations in results:

##### JAQueL (INNER JOINS)

    {
        "AoMeasurementQuantity": {},
        "$attributes": {
            "name": 1,
            "unit.name": 1,
            "quantity.name": 1
        },
        "$options": {
            "$rowlimit": 5
        }
    }

##### ods.SelectStatement ( joins )

    {
      "columns": [
        {
          "aid": "80",
          "attribute": "Name"
        },
        {
          "aid": "54",
          "attribute": "Name"
        },
        {
          "aid": "55",
          "attribute": "Name"
        }
      ],
      "joins": [
        {
          "aidFrom": "80",
          "aidTo": "54",
          "relation": "Unit"
        },
        {
          "aidFrom": "80",
          "aidTo": "55",
          "relation": "Quantity"
        }
      ],
      "rowLimit": "5"
    }

As you know, INNER JOINS behave like the overlap of a Venn diagram (when
visualizing it), so using INNER JOIN on 'unit' and 'quantity' relation
will only return results in case both relations are defined (not null).

Alternatively, you can also use OUTER JOINS (FULL OUTER JOIN):

##### JAQueL (OUTER JOINS)

    {
        "AoMeasurementQuantity": {},
        "$attributes": {
            "name": 1,
            "unit:OUTER.name": 1,
            "quantity:OUTER.name": 1
        },
        "$options": {
            "$rowlimit": 5
        }
    }

##### ods.SelectStatement (JT_OUTER)

    {
      "columns": [
        {
          "aid": "80",
          "attribute": "Name"
        },
        {
          "aid": "54",
          "attribute": "Name"
        },
        {
          "aid": "55",
          "attribute": "Name"
        }
      ],
      "joins": [
        {
          "aidFrom": "80",
          "aidTo": "54",
          "relation": "Unit",
          "joinType": "JT_OUTER"
        },
        {
          "aidFrom": "80",
          "aidTo": "55",
          "relation": "Quantity",
          "joinType": "JT_OUTER"
        }
      ],
      "rowLimit": "5"
    }

## JAQueL Language definitions

JAQueL has the following schema:

![QuerySchema](/images/QuerySchema.png)

    {
        "AoUnit": {
          "name": {
                "$like": "k*"
            },
        },
        "$orderby": {
            "name": 1
        },
        "$groupby": {
            "name": 1,
            "description": 1
        },
        "$options": {
            "$rowlimit": 5
        },
        "$attributes": {
            "name": 1,
            "description": {
                "$distinct": 1
            }
        }
    }

### Condition Operators

| JAQueL    | ASAM ODS OperatorEnum | remark                   |
| --------- | --------------------- | ------                   |
| $eq       | OP_EQ                 | equal                    |
| $neq      | OP_NEQ                | not equal                |
| $lt       | OP_LT                 | less than                |
| $gt       | OP_GT                 | greater than             |
| $lte      | OP_LTE                | less than or equal to    |
| $gte      | OP_GTE                | greater than or equal to |
| $in       | OP_INSET              | in set                   |
| $notinset | OP_NOTINSET           | not in set               |
| $like     | OP_LIKE               |                          |
| $null     | OP_IS_NULL            | empty/null value         |
| $notnull  | OP_IS_NOT_NULL        |                          |
| $notlike  | OP_NOTLIKE            |                          |
| $between  | OP_BETWEEN            |                          |

#### operator option

| JAQueL    | ASAM ODS OperatorEnum | remark                                                    |
| --------- | --------------------- | ------                                                    |
| "i"       | OP_CI_LIKE            | add as "option" for insensitive queries `"$options": "i"` |

### Condition Conjunctions

| JAQueL     | ASAM ODS ConjuctionEnum |
| ---------- | ----------------------- |
| $and       | CO_AND                  |
| $or        | CO_OR                   |
| $not       | CO_NOT                  |

### Condition Aggregates

| JAQueL     | ods.AggregateEnum     |
| ---------- | -----------------     |
| $none      | AG_NONE               |
| $count     | AG_COUNT              |
| $dcount    | AG_DCOUNT             |
| $min       | AG_MIN                |
| $max       | AG_MAX                |
| $avg       | AG_AVG                |
| $sum       | AG_SUM                |
| $distinct  | AG_DISTINCT           |
| $point     | AG_VALUES_POINT       |
| $ia        | AG_INSTANCE_ATTRIBUTE |

NOTE: Empty (NULL) attribute values are ignored for aggregates.

### Condition options

| JAQueL     | ASAM ods.proto               |
| ---------- | -----------------            |
| $options   |                              |
| $rowlimit  | SelectStatement.row_limit    |
| $rowskip   | SelectStatement.row_start    |
| $seqlimit  | SelectStatement.values_limit |
| $seqskip   | SelectStatement.values_start |

## License

Copyright © 2025 [Peak Solution GmbH](https://peak-solution.de)

The training material in this repository is licensed under a Creative Commons BY-NC-SA 4.0 license. See [LICENSE](../LICENSE) file for more information.
