package com.aulaSpring.webservice.resources;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.aulaSpring.webservice.entities.Product;
import com.aulaSpring.webservice.services.ProductService;

@RestController
@RequestMapping(value ="/products")
public class ProductResource {
    
    @Autowired
    private ProductService service;

    @GetMapping
    public ResponseEntity<List<Product>> findAll() {
        List<Product> Product = service.findAll();
        return ResponseEntity.ok().body(Product);
    }

    @GetMapping(value = "/{id}")
    public ResponseEntity<Product> findById(@PathVariable Long id) {
        Product Product = service.findById(id);
        return ResponseEntity.ok().body(Product);
    }
    
}
