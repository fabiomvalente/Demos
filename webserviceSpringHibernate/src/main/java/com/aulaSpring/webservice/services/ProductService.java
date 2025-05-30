package com.aulaSpring.webservice.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.aulaSpring.webservice.entities.Product;
import com.aulaSpring.webservice.repositories.ProductRepository;

@Service
public class ProductService {
    
    @Autowired
    private ProductRepository ProductRepository;

    public List<Product> findAll() {
        return ProductRepository.findAll();
    }

    public Product findById(Long id) {
        Optional<Product> obj = ProductRepository.findById(id);
        return obj.get();
    }
}
