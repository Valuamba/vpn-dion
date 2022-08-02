import {CardElement, useElements, useStripe} from "@stripe/react-stripe-js";
import React, {useState} from "react";

const CheckoutForm = () => {
  const [error, setError] = useState(null);
  const [email, setEmail] = useState('');

  const stripe = useStripe();
  const elements = useElements();// Handle real-time validation errors from the CardElement.

    const handleChange = (event) => {
    if (event.error) {
        setError(event.error.message);
    } else {
        setError(null);
    }
    }// Handle form submission.

const handleSubmit = async (event) => {
        event.preventDefault();
    };

return (
  <section>
			<div className='product'>
            <img
                src='https://i.imgur.com/EHyR2nP.png'
                alt='The cover of Stubborn Attachments'
            />
            <div className='description'>
                <h3>Stubborn Attachments</h3>
                <h5>$20.00</h5>
            </div>
        </div>
        <form
            action={`/api/stripe/create-checkout-session`}
            method='POST'
        >
            <button className='button' type='submit'>
                Checkout
            </button>
        </form>
    </section>
 );
};export default CheckoutForm;