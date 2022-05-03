# DocNets

## Inspiration

Doctors are life-savers, but saving life is only efficient if the patients reach them at time. So, we came up with a solution... To help patients reach out to their nearest, mostly affordable and specialized doctors, we developed an **instant, easy-to-use appointment manager.** 
Visit [DocNets](http://docnets.herokuapp.com/)

## What it does

Following are some of the short bulletins our web app does :-


- **We provide a user-friendly interface and messages.**

     Our web app provides a user-friendly interface with features like real-time maps and user-friendly messages to provide you help with what might be going wrong.

- **Enjoy Seem-less Real Time Scheduling.**

  Multiple Users can interact with booking system at the same time ! No Conflicts can occur in scheduling.

- **Sort the Doctors based on your needs.**

  Too many doctors to choose from? Sort them out based on their Experience, Fees or any other criteria you want ! Easy to work with as you just have to click on desired column

- **Availability of Doctor based on Location.**

  You can find the doctors based on their location, and make yourself comfortable with whichever location suits you best
  
 - **Easy and Quick Appointment Scheduling.**

    An Easy to Use and Fast Responding Appointment Scheduling System. Books conflict free appointments and gives user-friendly error messages if something is wrong.  

- **Use our easy to view Maps for location understandings**

  We also provide an easy-to-view instant maps for all our location services. This helps you as a user to have a quick view of the surrounding terrains of your appointment destination
  
- **Have any Problem? worry not we have FAQs Section.**

  If you feel stuck or have any problem, just visit our FAQs section for answers to some of our most common questions... Still Stuck? Visit our contact us page and reach out to us




## How we built it

Our frontend uses a mixture of Streamlit in its pure form along with some custom HTML, CSS and Javascript components.  
  
**Why we choose Streamlit?**  
     With Streamlit we got the power of Python 💪. Most of our frontend code is in python... which means this project has an infinite scope of expansion. (Since whatever python can do, we can do too).
_To know how python can be an advantage, how about visiting our website and trying to interact with all the beautiful real-time maps we support through python_ [DocNets](http://docnets.herokuapp.com/)

As for our backend, we purely used python, which goes well with Streamlit as its frontend partner.

For our real-time database support, we trusted Google Firebase for this job. Its one of the most easy-to-use, free (up to a limit which is usually high), secure and reliable cloud service for real-time databases.

Thanks to Folium. We were able to provide integration with real-time maps on our platform.


## Challenges we ran into

Although Streamlit uses python at its core. The community is still not too old, thus Streamlit lacks flexibility in some aspects. Although it still provides a way to import your custom made HTML, CSS and Javascript components, making them interact and fit beautifully in a website is a challenging task our frontend developers faced. But we cleared the hurdle neatly.
  
Efficient storing and processing different kinds of data was also a noticable challenge. But our team managed to resolve it by implementing and testing different approaches.

Of course tackling [Scope creep](https://en.wikipedia.org/wiki/Scope_creep) was a tough challenge.. especially in a team.

## Accomplishments that we're proud of

Our team worked hard for this project to be up and running in less than 3 days time. We feel proud that despite the pressure of our university sessionals, we successfully completed a full release after overcoming many challenges, performance issues and glitches. Also, we learnt many new things along the way.

## What we learned

Along our journey of this project we learnt lots of new features of Streamlit, Firebase Real-Time Database Management, Folium (for Map) and many other. Moreover, working on a team allowed all of us to discover great design patterns and code management tricks. With everyone working around the same problem, we found new ways to apply and fix our problems with some clever workarounds.

## What's next for DocNets

As mentioned earlier. With Streamlit and Python at the core of our frontend and backend, We have already exposed DocNets to a near infinite possibility of expansion. Some of the features we wish to add next are :- 

1. Expand our existing map service to provide a better metric of travelling distance from patient to doctor
2. Generating Reports for both doctor and patient
3. An online payment gateway
