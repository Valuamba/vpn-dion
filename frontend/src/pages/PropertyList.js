import React from 'react'
import { Alert, Col, Row, Spin} from 'antd'
import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import {  listProperties } from "../actions/propertyActions";

function PropertyListPage() {
    const dispatch = useDispatch();

    const propertiesList = useSelector((state) => state.propertiesList)

    const { loading, error, properties} = propertiesList

    useEffect((
        
    ) => {
        dispatch(listProperties())
    }, [dispatch])
  return (
    <>
        {loading ? (
            <div className='spinner'>
                <Spin size="large"/>
            </div>
        ) : error ? (
            <Alert type="error" message={error.message} showIcon className='alert-margin--top'/>
        ) : (
            <>
                <Row>
                    <Col span={24}>
                        <h2 className='margin--top'>Our Catalog of Properties</h2>
                    </Col>
                    {properties.map((property) => {
                        <Col key={property.id} securitym={12} md={6} lg={4} xs={3}>
                            <p>{property.title}</p>
                        </Col>
                    })}
                </Row>
            </>
        )}
    </>

  )
}

export default PropertyListPage;
