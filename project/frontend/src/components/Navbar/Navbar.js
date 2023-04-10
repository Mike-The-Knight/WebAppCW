import { Navbar } from 'react-bulma-components';

export default function CustomNavbar() {
   return (
      <Navbar>
         <Navbar.Brand>
            <Navbar.Item href="#">
               <img
                  alt="Bulma: a modern CSS framework based on Flexbox"
                  height="28"
                  src="https://bulma.io/images/bulma-logo.png"
                  width="112"
               />
            </Navbar.Item>
            <Navbar.Burger />
         </Navbar.Brand>
         <Navbar.Menu>
            <Navbar.Container>
               <Navbar.Item href="#">
                  <Navbar.Link>
                     First
                  </Navbar.Link>
                  <Navbar.Dropdown>
                     <Navbar.Item href="#">
                        Subitem 1
                     </Navbar.Item>
                     <Navbar.Item href="#">
                        Subitem 2
                     </Navbar.Item>
                     <Navbar.Divider />
                     <Navbar.Item href="#">
                        After divider
                     </Navbar.Item>
                  </Navbar.Dropdown>
               </Navbar.Item>
               <Navbar.Item href="#">
                  Second
               </Navbar.Item>
            </Navbar.Container>
            <Navbar.Container align="end">
               <Navbar.Item href="#">
                  At the end
               </Navbar.Item>
            </Navbar.Container>
         </Navbar.Menu>
      </Navbar>
   )
}