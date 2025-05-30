package com.aulaSpring.webservice.resources;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.aulaSpring.webservice.entities.Order;
import com.aulaSpring.webservice.services.OrderService;

@RestController
@RequestMapping(value ="/orders")
public class OrderResouce {
    
    @Autowired
    private OrderService service;

    @GetMapping
    public ResponseEntity<List<Order>> findAll() {
        // return ResponseEntity.ok("OK");
        // Order Order = new Order(1L, "Maria", "maria@example.com", "999999999", "123456");
        List<Order> Order = service.findAll();
        return ResponseEntity.ok().body(Order);
    }

    @GetMapping(value = "/{id}")
    public ResponseEntity<Order> findById(@PathVariable Long id) {
        Order Order = service.findById(id);
        return ResponseEntity.ok().body(Order);
    }
    
}
